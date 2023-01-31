import os
import shutil

from staticjinja import Site
from yaml import Loader, load


def data():
    return {
        "base": load(open("data/base.yaml"), Loader=Loader),
        "links": load(open("data/links.yaml"), Loader=Loader),
        "pages": load(open("data/pages.yaml"), Loader=Loader)
    }

def build_dir():
    shutil.rmtree("build")
    os.makedirs("build")

if __name__ == "__main__":

    site = Site.make_site()
    site.outpath="build"
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)

    shutil.copytree('static', 'build/static')