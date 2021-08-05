$( document ).ready(function() {
    $.ajaxSetup({
        data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
        },
    });

    $('#submit').click(function(){
        var code_input = $("#code_input").val();
        var parse_data = new FormData();
        parse_data.append('code_input',code_input);


        $.ajax({
            url:'/yeer/stock_search/ajax_stock/', 
            data:parse_data,  // 傳到後端的資料
            type:'POST',
            dataType: 'json',
            processData:false,
            contentType:false,
            success:function(data)
            { //後端傳來的jsonresponse
                document.getElementById('stock').innerHTML = '<h3>' + data.stock_name + code_input + '</h3>';
            },
            error: function()
            {
                alert('Something error');
            },

        });

    })

    });
