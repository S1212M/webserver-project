from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>My DevOps Server</title>
            <style>
                body {
                    font-family: Arial;
                    background-color: #1e1e2e;
                    color: white;
                    text-align: center;
                    padding: 50px;
                }
                h1 { color: #89b4fa; }
                .card {
                    background-color: #313244;
                    padding: 20px;
                    border-radius: 10px;
                    margin: 20px auto;
                    width: 50%;
                }
                .green { color: #a6e3a1; }
                .yellow { color: #f9e2af; }
            </style>
        </head>
        <body>
            <h1>My DevOps Server</h1>
            <div class="card">
                <h2 class="green">Server is Running!</h2>
                <p>Deployed using Docker + Jenkins CI/CD Pipeline</p>
            </div>
            <div class="card">
                <h2 class="yellow">Tech Stack</h2>
                <p>Linux | Shell Scripting | Git | Docker | Jenkins</p>
            </div>
            <div class="card">
                <h2>Built by Saurabh Maurya</h2>
                <p>DevOps Engineer in the making </p>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html.encode())

    def log_message(self, format, *args):
        pass

HTTPServer(('0.0.0.0', 7000), Handler).serve_forever()
