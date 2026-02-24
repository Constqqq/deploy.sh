from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK") # То, что ждет скрипт
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello from Docker!")

print("Server started on port 8000...")
HTTPServer(('0.0.0.0', 8000), SimpleHandler).serve_forever()