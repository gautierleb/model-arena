"""Serve the page: python -m app [port] (default 8000), on 127.0.0.1 only."""

import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from app import page


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        found = self.path.split("?")[0] == "/"
        body = (page() if found else "not found").encode()
        self.send_response(200 if found else 404)
        self.send_header("Content-Type", "text/html; charset=utf-8" if found else "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
