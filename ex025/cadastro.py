from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MeuServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        caminho_arquivo = os.path.join(os.path.dirname(__file__), 'form003.html') # mudar o nome do arquivo no caminho para reaproveitar este servidor http em outros exercícios

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        with open(caminho_arquivo, 'rb') as arquivo:
            self.wfile.write(arquivo.read())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'<h1>Os dados foram enviados!</h1>')


server = HTTPServer(('localhost', 8000), MeuServidor)
print("Servidor rodando em http://localhost:8000")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Encerrando servidor...")
    server.server_close()