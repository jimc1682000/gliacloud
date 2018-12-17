from http.server import BaseHTTPRequestHandler, HTTPServer
import zen

PORT_NUMBER = 80
class zenHandler(BaseHTTPRequestHandler):
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(zen.getZen())
		return
try:
	server = HTTPServer(('', PORT_NUMBER), zenHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()