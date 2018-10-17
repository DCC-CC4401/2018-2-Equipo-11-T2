(function($){
    $(function(){
        $('.sidenav').sidenav();
        $('.collapsible').collapsible();
        $(document).ready(function(){
            $('.tabs').tabs();
        });
        $(document).ready(function(){
            $('.datepicker').datepicker();
        });
        $('.dropdown-trigger').dropdown();
    }); // end of document ready
})(jQuery); // end of jQuery name space
