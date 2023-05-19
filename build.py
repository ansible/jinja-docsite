import os
import shutil
import sass

from pathlib import Path
from staticjinja import Site
from yaml import Loader, load

def data():
    return {
        "base": load(open("data/base.yaml"), Loader=Loader),
        "ecosystem": load(open("data/ecosystem.yaml"), Loader=Loader),
        "links": load(open("data/links.yaml"), Loader=Loader),
        "pages": load(open("data/pages.yaml"), Loader=Loader)
    }

buildpath = Path('build')
if buildpath.exists() and buildpath.is_dir():
    shutil.rmtree("build")

if __name__ == "__main__":

    site = Site.make_site()
    site.outpath="build"
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)


    shutil.copytree('static', 'build/static')
    shutil.move('build/ecosystem.html', 'build/index.html')
    sass.compile(dirname=('sass', 'build/static/css'))
