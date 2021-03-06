#!/usr/bin/env python
#
# Copyright (c) 2017 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rake import RakeKeywordExtractor;
import MySQLdb
from dbutils import DBConfig
import sys
import re
import pandas.io.sql as sql
import nltk

if len(sys.argv) < 4:
    print("you must provide a question id , a max number of tags, delete param and working dir")
    exit(-1)

working_dir = sys.argv[1]  # param
question_id = int(sys.argv[2])  # param
max_tags = int(sys.argv[3])  # param
must_delete_former_automatic_tags = int(sys.argv[4])  # param

download_dir="/tmp/nltk_data"
# resources download
nltk.download('stopwords', download_dir)
nltk.download('punkt', download_dir)
nltk.download('averaged_perceptron_tagger', download_dir)
nltk.download('wordnet', download_dir)
nltk.download('pickle', download_dir)

rake = RakeKeywordExtractor();

TAG_TYPE = "AUTOMATIC"
queryTag = "SELECT ID FROM SurveyAnswerTag WHERE Type='AUTOMATIC' AND Value = '%s' "
queryInsertTag = "INSERT INTO SurveyAnswerTag (Created,LastEdited, Value, Type, CreatedByID) VALUES(NOW(), NOW(), '%s', 'AUTOMATIC', 0 )"
queryAnswers = "SELECT ID, Value FROM SurveyAnswer WHERE Value IS NOT NULL AND QuestionID = %d"
queryInsertAnswerTag = "INSERT INTO SurveyAnswer_Tags(SurveyAnswerID, SurveyAnswerTagID) VALUES(%d, %d)"
querySelectAnswerTag = "SELECT ID FROM SurveyAnswer_Tags WHERE SurveyAnswerID = %d AND SurveyAnswerTagID = %d"
queryDeleteFormerTags = "DELETE FROM SurveyAnswer_Tags WHERE SurveyAnswerID = %d AND SurveyAnswerTagID IN (SELECT ID FROM SurveyAnswerTag where Type = 'AUTOMATIC')"

config = DBConfig(working_dir+"/db.ini").read_db_config()

cursor = None

try:
    # Open database connection
    db = MySQLdb.connect(**config)

    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    data = sql.read_sql(queryAnswers % question_id, db)
    for idx, answer in enumerate(data['Value'].tolist()):
        keywords = rake.extract(answer)
        answerId = data['ID'].values[idx]
        if must_delete_former_automatic_tags > 0:
            cursor.execute(queryDeleteFormerTags % (answerId))
        # tag processing
        for idx2, tag in enumerate(keywords[:max_tags]):
            tag = re.sub(r"[^\w\d]", "", tag)
            if len(tag) > 2:
                cursor.execute(queryTag % (tag))
                dbTag = cursor.fetchone()
                tagId = None
                if dbTag is None:
                    res = cursor.execute(queryInsertTag % (tag))
                    tagId = cursor.lastrowid
                else:
                    tagId = dbTag[0]
                cursor.execute(querySelectAnswerTag % (answerId, tagId))
                existAnswerTag = cursor.fetchone();
                if existAnswerTag is None:
                    cursor.execute(queryInsertAnswerTag % (answerId, tagId))

    db.commit()
except Exception as e:
   print(e)
   # Rollback in case there is any error
   db.rollback()
   raise
finally:
    # disconnect from server
    db.close()
    if not (cursor is None):
        cursor.close()