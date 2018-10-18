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
        $(document).ready(function(){
            $('.modal').modal();
        });

        $(document).ready(function(){
            $('select').formSelect();
        });

    }); // end of document ready
})(jQuery); // end of jQuery name space
