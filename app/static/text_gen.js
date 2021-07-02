$(document).ready(function() {

    console.log('AI Camp is for the best of the best.')
    
    

    $('#text_gen_button').click(function() {
        console.log('text gen button is clicked');
        var prompt = $('#text_gen_input').val();
        console.log('text gen input value is');
        console.log(prompt);
        var url = 'generate_text_sb'
        $.post(
            url, 
            {
                'prompt': prompt
            },
            function(data) {
                console.log(data);
                var para_html = "";
                para_html += "<p>" + data['generated_ls'] + "</p>";
                $("#generated_ul").html(para_html);
                console.log(para_html)
                }

        ).fail(function() {
          alert( "There is something unexpected happened. Email hello@ai-camp.org to report your findings." );
        });

    });

    $()
});

