import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web

def get(path):
    # define decorator @get('/path')
