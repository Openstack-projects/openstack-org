<?php

/* 
   Static content page for Austin
*/

class SummitStaticAboutPage extends SummitPage {

}


class SummitStaticAboutPage_Controller extends SummitPage_Controller {

    public function init()
    {
        $this->top_section = 'full';
        parent::init();
        Requirements::block("summit/css/combined.css");
        Requirements::css("themes/openstack/css/static.combined.css");
    }


}