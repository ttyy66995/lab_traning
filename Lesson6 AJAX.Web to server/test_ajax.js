$( document ).ready(function() {
    $.ajaxSetup({
        data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
        },
    });

    $('#submit').click(function(){

        var name = $("#Name").val();
        var comments = $("#Comments").val();
        var number1 = $("#Number1").val();
        var number2 = $("#Number2").val();

        var parse_data = new FormData();

        parse_data.append('name',name);
        parse_data.append('comments',comments);
        parse_data.append('number1',number1);
        parse_data.append('number2',number2);

        $.ajax({
            url:'/yee_project/ajax/ajax_test/', 
            data:parse_data,  // 傳到後端的資料
            type:'POST',
            dataType: 'json',
            processData:false,
            contentType:false,
            success:function(data)
            { //後端傳來的jsonresponse
                
                var result_name = data.result_name;
                var result_comments = data.result_comments;
                var result_number = data.result_number;

                console.log(result_name,result_comments,result_number)

                document.getElementById("result_name").innerHTML = result_name;
                document.getElementById("result_comments").innerHTML = result_comments;
                document.getElementById("result_number").innerHTML = result_number;

            },
            error: function()
            {
                alert('Something error');
            },
    
         });

    })
    
});