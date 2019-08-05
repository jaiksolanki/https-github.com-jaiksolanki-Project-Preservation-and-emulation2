$('.message a').click(function(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});


$(function() {
    $('.login').click(function() {
        var user = $('#username').val();
        var pass = $('#password').val();
        $.ajax({
            url: '/loginUser',
            data: $('#login-form').serialize(),
            async: false,
            type: 'POST',
            dataType: 'json',
            success: function(response) {
                var obj = JSON.parse(response)
                if(response.status=='OK'){
                    window.location.replace("/dashboard");
                    console.log(response.status);
                }
                else
                    window.location.replace("templates/slogin.html");
                console.log(obj.status);
            },
            error: function(error) {

                console.log(error);
            }
        });
    });
});
