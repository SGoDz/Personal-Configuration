#!/usr/bin/env python
import smtpd
import asyncore

class CustomSMTPServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        print 'Receiving message from:', peer
        print 'Message addressed from:', mailfrom
        print 'Message addressed to  :', rcpttos
        print 'Message length        :', len(data)
        print 'Message data          :', data
        return

server = CustomSMTPServer(('127.0.0.1',25), None)
asyncore.loop()