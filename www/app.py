import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(
        body=b'<h1>Awesome</h1>\n',
        content_type='text/html',
        charset='utf-8',
    )

def hello(request):
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(
        body=text.encode('utf-8'),
        content_type='text/html',
        charset='utf-8',
    )

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    logging.info('server started at localhost:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
