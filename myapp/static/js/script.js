tbody = document.getElementsByTagName("tbody")[0];
var trs = tbody.getElementsByTagName("tr");
var tds = null;

for (var i=0; i<trs.length; i++)
{
    tds = trs[i].getElementsByTagName("td");
    for (var n=0; n<tds.length;n++)
    {
        tds[n].innerHTML+='<button id="record" onclick="myFunction(this)">Record</button>'
    }
}
function myFunction(elem) {
    var SpeechRecognition = window.webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
    var Textbox = elem.previousSibling.previousSibling.previousSibling;
    var Content = ' ';

    recognition.continuous = false;
    recognition.start();

    recognition.onresult = function(event) {
    var current = event.resultIndex;
    var transcript = event.results[current][0].transcript;
        Content += transcript;
        Textbox.value+=Content;
    };

}