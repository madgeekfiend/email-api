$(document).ready(function() {

    // Will use this in the jQuery post function - DRY
    // If you pass in true it will clear the output
    function clearForm(clearOutput) {
        $("input[type=text], textarea, input[type=file]").val("");  
        if (clearOutput) {
            $('#email-parse-output').empty();
        }
    }

    function successDisplayHtml(data) {
        console.log("Received data " + data);
        console.log(data);
        var resultHtml = "<table><col width='20%'><col width='80%'><tr><td>To: " + data.to.join(' ') + "</td></tr><tr><td>From: " + data.from.join(' ') +"</td></tr> \
        <tr><td>Subject: " + data.subject + "</td></tr><tr><td>Date: " + data.date + "</td></tr></table>";
        console.log(resultHtml);
        $('#email-parse-output').html(resultHtml);
    }

    // Bind to reset button and clear reset the form
    $('#reset-form').bind("click", function(event) {
        event.preventDefault();
        clearForm(true);      
    })

    $('form#email-form').on('submit', function(event) {
        event.preventDefault();
        var $form = $('#email-form');

        if ($form[0].file.files.length == 0) {
            $.ajax({
                url : "http://localhost:5000/api/v1/email/parse",
                type: "POST",
                data: JSON.stringify({"emailRawText": $('#emailMessageInput').val(), "emailFile":''}),
                contentType: "application/json; charset=utf-8",
                dataType   : "json",
                success    : function(data) {
                    successDisplayHtml(data);
                }
            });
        } 
        else
        {
            // Assume a file is attached and upload the file
            var formData = new FormData();
            formData.append('file', $('input[type=file]')[0].files[0]);
            formData.append('emailRawText', '');
            $.ajax({
                url : "http://localhost:5000/api/v1/email/parse",
                type: "POST",
                data: formData,
                contentType: false,
                processData   : false,
                success    : function(data){
                    successDisplayHtml(data);
                }
            });
        }

        // Reset the form
        clearForm(false);
    })

})