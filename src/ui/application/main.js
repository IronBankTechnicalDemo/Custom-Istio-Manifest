$(function() {
    $('#get_all').click(function() {
        $.get( "http://localhost:5000/objects", function( data ) {
            var list = "";
            $.each(data.objects, function() {
                console.log(this);
                list = list + "<li>" + this + "</li>";
            });

            $('#all_list').html(list);
        });
    });

    $('#create').click(function() {
        $.ajax({
          type: "POST",
          url: 'http://localhost:5000/objects',
          data: JSON.stringify({
            firstName: $('#first_name').val(),
            lastName: $('#last_name').val()
          }),
          success: function(data) {
              alert('Created');
          },
            contentType: 'application/json',
            dataType: 'json'
        });
    });

    $('#get_object').click(function() {
        $.get( "http://localhost:5000/objects/" + $('#get_id').val(), function( data ) {
            console.log(data);
            $('#id').val(data.object.id);
            $('#first_name').val(data.object.firstName);
            $('#last_name').val(data.object.lastName);
        });
    });

        $('#update_object').click(function() {
        $.ajax({
          type: "DELETE",
          url: 'http://localhost:5000/objects/' + $('#id').val(),
          data: JSON.stringify({
            id: $('#id').val(),
            firstName: $('#first_name').val(),
            lastName: $('#last_name').val()
          }),
          success: function(data) {
              alert('Created');
          },
            contentType: 'application/json',
            dataType: 'json'
        });
    });


    $('#delete_object').click(function() {
        $.ajax({
          type: "DELETE",
          url: 'http://localhost:5000/objects/' + $('#delete_id').val(),
          success: function(data) {
              alert('Deleted');
          },
            dataType: 'json'
        });
    });

});