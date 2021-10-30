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
    
    async def prepare(self):
        self.uuid = str(uuid.uuid4())
        print(f"Got request {self.uuid}")
        print(f"Processing request...")
        self.set_header("x-request-id", self.uuid)
        await asyncio.sleep(self.timesleep)
    
    async def get(self):
        self.write("GET: Hello world")
    
    async def post(self):
        self.write("POST: Hello world")
    
    def on_finish(self) -> None:
        print(f"request {self.uuid} processed.")
        
        return super().on_finish()


def build_app():
    handlers = [
        (r"/", MainHandler, dict(timesleep=1))
        ]
    
    app = WebServer(handlers=handlers, debug=True)
    
    return app
    
        

