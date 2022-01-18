from aiohttp import web
import aiohttp_jinja2
import jinja2


def setup_router(application):
    from bac_app.forum.routes import setup_router as setup_forum_router
    setup_forum_router(application)

def setup_external_library(application: web.Application) -> None:
    aiohttp_jinja2.setup(application, loader=jinja2.FileSystemLoader("templates"))

def setup_app(application):
    setup_router(application)
    setup_external_library(application)

app = web.Application()

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app)