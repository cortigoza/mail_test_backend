import mail_http
from tornado import httpserver
from tornado import autoreload
from tornado.ioloop import IOLoop


def main():
    print("starting service")
    app = mail_http.mail_handlers()
    server = httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)  # Forks multiple sub-processes
    autoreload.start()
    IOLoop.current().start()


if __name__ == "__main__":
    main()
