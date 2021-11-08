import asyncio
from re import DEBUG
from typing import Optional, List
import tornado.ioloop
import tornado.web
import uuid


class WebServer(tornado.web.Application):
    def __init__(self, handlers, default_host: Optional[str] = None, transforms: Optional[List] = None, **settings):
        super().__init__(handlers=handlers, default_host=default_host, transforms=transforms, **settings)
    
    def run(self, port=8888):
        self.listen(port)
        tornado.ioloop.IOLoop.current().start()
    
    def stop(self):
        tornado.ioloop.IOLoop.current().stop()
    

class MainHandler(tornado.web.RequestHandler):
    def initialize(self, timesleep):
        self.timesleep = timesleep
        self.body = None
    
    async def prepare(self):
        self.uuid = str(uuid.uuid4())
        print(f"Got request {self.uuid}")
        print("Request header:")
        print(self.request.headers)
        print()
        self.set_header("x-request-id", self.uuid)
        await asyncio.sleep(self.timesleep)
        if self.request.body:
            if self.request.headers.get("content-type") == "application/json":
                self.body = self.request.body.decode('utf-8')
    
    async def get(self):
        self.write("GET: Hello world")
    
    async def post(self):
        self.write("POST: Hello world")
        print("Raw body", self.request.body)
        print("Decoded body", self.body)
    
    def on_finish(self) -> None:
        print(f"request {self.uuid} processed.")
        
        return super().on_finish()


def build_app():
    handlers = [
        (r"/", MainHandler, dict(timesleep=0.1))
        ]
    
    app = WebServer(handlers=handlers, debug=True)
    
    return app
    
        

