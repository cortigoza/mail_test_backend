import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers",
                        "x-requested-with, Content-Type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def post(self):
        self.write({})

    def get(self):
        self.write({})

    def options(self):
        # no body
        self.set_status(204)
        self.finish()

    def writeResponse(self, response):
        if 'error' in response:
            self.set_status(500)
        self.write({"data": response})
        self.finish()
