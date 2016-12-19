from stomp import *
c = Connection([('127.0.0.1', 61616)])
c.set_listener('', PrintingListener())
c.start()
c.connect('admin', 'admin', wait=True)

c.subscribe('/queue/haciaZWP', 123)
c.send('/queue/haciaZWP', 'a test message')
