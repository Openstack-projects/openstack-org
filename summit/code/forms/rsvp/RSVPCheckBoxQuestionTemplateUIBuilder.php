<?php
/**
 * Copyright 2015 OpenStack Foundation
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 **/

/**
 * Class RSVPCheckBoxQuestionTemplateUIBuilder
 */
class RSVPCheckBoxQuestionTemplateUIBuilder
    extends AbstractRSVPQuestionTemplateUIBuilder {

    /**
     * @param IRSVPQuestionTemplate $question
     * @param ?IRSVPAnswer $answer
     * @param ?IRSVP $rsvp
     * @return FormField
     */
    public function build(IRSVPQuestionTemplate $question, ?IRSVPAnswer $answer, ?IRSVP $rsvp)
    {
        $field = new CheckboxField($question->name(), $question->label());
        $field->setValue($question->initialValue());
        if($question->isReadOnly()) $field->setDisabled(true);
        if($question->isMandatory())
        {
            $field->setAttribute('data-rule-required','true');
        }
        if(!is_null($answer)){
            $field->setValue($answer->value());
        }

        $field->setFieldHolderTemplate('RSVPCheckboxField_holder');

        return $field;
    }
}