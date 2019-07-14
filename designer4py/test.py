""" Testing module """
from flask import Flask
from designer4py.tools import Page, Canvas

app = Flask(__name__)


class PageTest:

    _page = None
    _canvas = None

    def __init__(self):
        pass

    def show_layout(self):
        self._canvas = Canvas('test')
        self._page = Page(self._canvas)
        return self._page.render()


def start_app():
    p = PageTest()
    app.add_url_rule('/', 'index', p.show_layout)
    app.run(host='127.0.0.1', port='5001')


if __name__ == "__main__":
    start_app()
