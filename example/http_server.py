import http.server
import socketserver

PORT = 8080

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    pass

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()