import os
import shutil
import sass

from pathlib import Path
from staticjinja import Site
from yaml import Loader, load

def data():
    return {
        "base": load(open("data/base.yaml"), Loader=Loader),
        "links": load(open("data/links.yaml"), Loader=Loader),
        "pages": load(open("data/pages.yaml"), Loader=Loader),
        "projects": load(open("data/projects.yaml"), Loader=Loader)
    }

buildpath = Path('build')
if buildpath.exists() and buildpath.is_dir():
    shutil.rmtree("build")

shutil.copyfile('templates/community.html', 'templates/ansible_community.html')
shutil.copyfile('templates/platform.html', 'templates/automation.html')
shutil.copyfile('oldsite/automation.html', 'oldsite/platform.html')

if __name__ == "__main__":

    site = Site.make_site()
    site.outpath="build"
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)


    shutil.copytree('static', 'build/static')
    shutil.copytree('oldsite', 'build/oldsite')
    sass.compile(dirname=('sass', 'build/static/css'))
