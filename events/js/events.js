jQuery(document).ready(function($){
    refresh_future_events_scroll();
    setInterval(refresh_page,60000);
});

function refresh_page() {
    refresh_future_events();
    refresh_future_summits();
    refresh_past_summits();
}

function refresh_future_events_scroll(){
    var second_column = jQuery('div.events-second-column');
    if(second_column.length>0){
        var upcoming_events_container = jQuery('#upcoming-events-container');
        if(upcoming_events_container.length>0){
            upcoming_events_container.css('max-height', ( second_column.height() ) +'px');
            upcoming_events_container.css('overflow-y','auto');
            upcoming_events_container.css('overflow-x','none');
        }
    }
}

function refresh_future_events() {
    jQuery.ajax({
        type: "POST",
        url: 'EventHolder_Controller/AjaxFutureEvents',
        success: function(result){
           jQuery('.single-event','#upcoming-events').remove();
           jQuery('#upcoming-events'). append(result);
           refresh_future_events_scroll();
        }
    });
}

function refresh_future_summits() {
    jQuery.ajax({
        type: "POST",
        url: 'EventHolder_Controller/AjaxFutureSummits',
        success: function(result){
            jQuery('.single-event','#future-summits').remove();
            jQuery('#future-summits').append(result);
        }
    });
}

function refresh_past_summits() {
    jQuery.ajax({
        type: "POST",
        url: 'EventHolder_Controller/AjaxPastSummits',
        success: function(result){
            jQuery('.single-event','#past-summits').remove();
            jQuery('#past-summits').append(result);
        }
    });
}