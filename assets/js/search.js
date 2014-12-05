function showResponse(response) {
	// for(var i=0;i<response.urls.length;i++)
    // {
        var snipobj = response.urls[0];
        document.getElementById('response').innerHTML += "<br>" +
        		"<div class='row-fluid'>" +
        			"<div class='span12'" + snipobj.url.substr(19) +
                "</div>";
    
    document.getElementById('response').innerHTML += '<br><br>';
}

function search() {
    document.getElementById('response').innerHTML = "";
    var xhr = new XMLHttpRequest();
    var url = document.getElementById('query').value;    
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
        	showResponse(JSON.parse(xhr.responseText));
        }
    }
    xhr.open("GET", "scrape/?url=" + url, false);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send();
    xmlDocument = xhr.responseText;
}
