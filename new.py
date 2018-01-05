from BaseHTTPServer import BaseHTTPRequestHandler , HTTPServer
import SimpleHTTPServer
PORT=10023
class AjaxHandler ( SimpleHTTPServer . SimpleHTTPRequestHandler ):
    def do_POST (self):
        self. send_response (200)
        self. send_header ('Content-type','text/html')
        self. send_header ('Access-Control-Allow-Origin','*')
        self. end_headers ()
# Send the html message
        self. wfile . write ("Ahmad Hassan,161AEB023 ")
        return
try:
    server =HTTPServer (('',PORT), AjaxHandler )
    print 'Started AJAX handler on port',PORT
    server . serve_forever ()
except KeyboardInterrupt :
    print '^C received , shutting down the web server '
    server.socket.close ()
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AJAX:Ahmad Hassan</title>
</head>

<body>
   161AEB023
    <form name="main_form" method="post">
        <input type="text" name="student_id" value="0" size="9">
        <input type="submit" onClick="button_press();" value="start" title="start">
    </form>

    Student data is <span id="result_span" style="color:red"> - </span>
</body>
<!--===============================================-->
<script type="text/javascript">
    //---------------------------------------------
    //Request sender
    function xml_http_post(url, data, callback) {
        var req = new XMLHttpRequest();
        req.open("POST", url, true);
        req.onreadystatechange = function() {
            if (req.readyState == 4) {
                callback(req);
            }
        }
        req.send(data);
    }
    //---------------------------------------------
     
   
    //---------------------------------------------
    // Display result
    function display_result(req) {
        var elem = document.getElementById('result_span')
        elem.innerHTML = req.responseText
    }

    // button press causes request via network
    function button_press() {
        var data = document.main_form.student_id.value;
        var port = '10' + data.slice(-3);
        xml_http_post ("http://213.175.92.37:"+port , data , display_result);
    }
    //---------------------------------------------
</script>
</html>

