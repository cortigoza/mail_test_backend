from services.mail import mailCore


class Premium(mailCore):
    def sendHTML(self, data):
        data['request']['content_type'] = "html"
        return mailCore.send(self, data)
