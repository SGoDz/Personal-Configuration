import stomp
import sys

conn = stomp.Connection([('127.0.0.1', 61613)])
conn.start()
conn.connect( 'admin','admin' )

conn.subscribe( destination='/queue/test', id=1, ack='auto' )

conn.send( body='hola mundo pam'.join(sys.argv[1:]), destination='/queue/test')

conn.disconnect()
