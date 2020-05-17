import json
import traceback
from lib import base_handler
from tornado import web
from services.basic import Basic
from services.premium import Premium


class MailPremium(base_handler.BaseHandler):
    def post(self):
        try:
            # ordering info format json
            premium = json.loads(self.request.body)
            response = Premium(premium).sendHTML(premium)
            self.writeResponse(response)
        except Exception:
            print(traceback.format_exc())
            self.writeResponse({"response": "error envio"})


class MailBasic(base_handler.BaseHandler):
    def post(self):
        try:
            basic = json.loads(self.request.body)  # ordering info format json
            response = Basic(basic).sendText(basic)
            self.writeResponse(response)
        except Exception:
            print(traceback.format_exc())
            self.writeResponse({"error": "error envio"})


class HealthBaseHandler(base_handler.BaseHandler):
    def get(self):
        self.writeResponse({"status": "Mail service is running"})


class mail_handlers(web.Application):
    def __init__(self):
        handlers = [
            (r"/premium", MailPremium),
            (r"/basic", MailBasic),
            (r"/health", HealthBaseHandler)
        ]
        web.Application.__init__(self, handlers)
