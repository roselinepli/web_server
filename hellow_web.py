"""
1. Wait for someone to connect to our server and send an HTTP request;
2. Parse that request;
3. Fifure our what it's asking for;
4. Fetch that data(or generate it dynamically);
5. Format the data as HTML;
6. Send it back.
Steps 1, 2 and 6 are the same from one application to another, so the Python library has a module called BaseHTTPServer
that does those for us. We just have to take care of steps 3-5.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''

    # Page to send back.
    Page = '''\
<html>
<body>
<p>Hello, web!</p>
</body>
</html>
'''
    # Handle a GET request.
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(self.Page)))
        self.end_headers()
        self.wfile.write(self.Page)

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()