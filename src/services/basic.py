from services.mail import mailCore


class Basic(mailCore):
    def sendText(self, data):
        data['request']['content_type'] = "plain"
        return mailCore.send(self, data)
