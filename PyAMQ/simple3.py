from stomp import *
c = Connection([('127.0.0.1', 8161)])
c.set_listener('', PrintingListener())
c.start()
c.connect('admin', 'admin')
c.subscribe(destination='/queue/test', id=1, ack='auto')
c.send( '/queue/test', 'a test message')
