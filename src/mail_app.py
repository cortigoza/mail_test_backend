import mail_http
import tornado.httpserver
from tornado.ioloop import IOLoop
import tornado.autoreload


def main():
    print("starting service")
    app = mail_http.mail_handlers()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start(0)  # Forks multiple sub-processes
    tornado.autoreload.start()
    IOLoop.current().start()


if __name__ == "__main__":
    main()
