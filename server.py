import os
import sys
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 3000

class LisaHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        '.glb': 'model/gltf-binary',
        '.gltf': 'model/gltf+json',
        '.exr': 'image/x-exr',
        '.woff2': 'font/woff2',
        '.woff': 'font/woff',
        '.m3u8': 'application/vnd.apple.mpegurl',
        '.mp3': 'audio/mpeg',
        '.mp4': 'video/mp4',
        '.svg': 'image/svg+xml',
    }

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run_server():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, LisaHandler)
    url = f"http://localhost:{PORT}"
    print("=" * 60)
    print(f" Locomotive® L.I.S.A - Local Clone Server")
    print(f" URL: {url}")
    print(" Tekan Ctrl+C untuk menghentikan server.")
    print("=" * 60)
    
    if "--open" in sys.argv:
        webbrowser.open(url)
        
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer dihentikan.")

if __name__ == "__main__":
    run_server()
