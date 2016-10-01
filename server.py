import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
import socket

from changeSlides import Slide

PORT = 8888
app = Slide()


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Connection Open.")

    def on_message(self, message):
        print(message)
        # print("hello")
        app.main_loop(message)
        # print App.main_loop(numpy.array(image))['bpm']

    def on_close(self):
        print("Connection Closed.")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r'/websocket', WebSocketHandler)]
        tornado.web.Application.__init__(self, handlers)


if __name__ == '__main__':
    ws_app = Application()
    server = tornado.httpserver.HTTPServer(ws_app)
    server.listen(PORT)
    hostIP = socket.gethostbyname(socket.gethostname())
    print('*** Websocket Server Started at %s:%d***' % (hostIP, PORT))
    tornado.ioloop.IOLoop.instance().start()
