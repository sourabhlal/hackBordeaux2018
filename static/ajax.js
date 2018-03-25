function refreshView() {
    $.ajax({
        url: "/refreshView",
        data: {},
        success: function( result ) {
            var obj = $.parseJSON(result);
            console.log(obj.current_view)
            $( "#room" ).html( "<img src="+obj.current_view+" class='img-fluid img-responsive'>" );
            console.log(obj.discovered_clues)
        }
    });
    setTimeout(refreshView, 1000); 
  }
  
  $(document).ready(function() {
    setTimeout(refreshView, 1000);
  });