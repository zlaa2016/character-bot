/* get response script */
$(document).ready(function() {
    console.log('chatbot js loaded.')
        function getBotResponse() {
          var rawText = $('#text_gen_input').val();
          var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
          var url = 'generate_text_sb';
          $('#text_gen_input').val("");
          $("#chatbox").append(userHtml);
          document
            .getElementById("text_gen_input")
            .scrollIntoView({ block: "start", behavior: "smooth" });

          $.post( url, 
                { prompt: rawText 
                
          }).done(function(data) {
            var botHtml = '<p class="botText"><span>' + data['generated_ls'] + "</span></p>";
            $("#chatbox").append(botHtml);
            console.log('bot text added');
           document
              .getElementById("text_gen_input")
              .scrollIntoView({ block: "start", behavior: "smooth" });
          });
        }
        $("#text_gen_input").keypress(function(e) {
          if (e.which == 13) {
            getBotResponse();
          }
        });
  
  });