from tornado import httpserver, gen
import simplejson as json
import traceback
from services.basic import Basic
from services.premium import Premium
import tornado.web


class MailPremium(tornado.web.RequestHandler):
    def post(self):
        try:
            # ordering info format json
            premium = json.loads(self.request.body)
            response = Premium(premium).sendHTML(premium)
            self.write({response})
        except Exception:
            print(traceback.format_exc())
            self.write({"response": "error envio"})


class MailBasic(tornado.web.RequestHandler):
    def post(self):
        try:
            basic = json.loads(self.request.body)  # ordering info format json
            response = Basic(basic).sendText(basic)
            self.write({response})
        except Exception:
            print(traceback.format_exc())
            self.write({'error': 'error envio'})


class HealthBaseHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({"status": "Mail service is running"})


class mail_handlers(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/premium", MailPremium),
            (r"/basic", MailBasic),
            (r"/health", HealthBaseHandler)
        ]
        tornado.web.Application.__init__(self, handlers)
