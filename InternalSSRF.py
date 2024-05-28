from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request for {self.path} from {self.client_address[0]}:{self.client_address[1]}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Check your terminal, you should have received a request from SSRF vulnerable webapp.')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received POST request for {self.path} from {self.client_address[0]}:{self.client_address[1]}")
        print(f"Data: {post_data}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Received POST request.')

if __name__ == '__main__':
    httpd = HTTPServer(('0.0.0.0', 8585), SimpleHTTPRequestHandler)
    print("HTTP server running on port 8585, Listening to a potential SSRF vulnerable app. \nUse URL: http://ThisIP:8585")
    httpd.serve_forever()
