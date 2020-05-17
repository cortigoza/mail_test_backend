import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64


class mailCore:
    def __init__(self, data):
        settings = data['settings']
        mandatory_args = ["user", "password",
                          "server", "port"]  # required send
        for x in mandatory_args:
            if settings.get(x, False) == False:
                raise ValueError("%s must be provided" % (x))
            self.__dict__[x] = settings[x]

    def send(self, data):
        print(self)
        request = data['request']
        mandatory_args = ["subject", "from", "to",
                          "content", "content_type"]  # required
        for x in mandatory_args:
            if not request.get(x, False):
                raise ValueError("%s is mandatory" % (x))

        msg = MIMEMultipart('alternative')
        msg['Subject'] = request['subject']
        msg['From'] = request['from']
        msg['To'] = request['to']
        content = MIMEText(request['content'], request['content_type'])
        msg.attach(content)

        password = base64.b64decode(self.password).decode('UTF-8')

        server = smtplib.SMTP(host=self.server, port=self.port)
        server.starttls()

        server.login(self.user, password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        return "ok"
