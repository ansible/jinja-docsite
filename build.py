import os
import shutil
import sass

from pathlib import Path
from staticjinja import Site
from yaml import Loader, load

def data():
    return {
        "base": load(open("data/base.yaml"), Loader=Loader),
        "developers": load(open("data/developers.yaml"), Loader=Loader),
        "community": load(open("data/community.yaml"), Loader=Loader),
        "ecosystem": load(open("data/ecosystem.yaml"), Loader=Loader),
        "index": load(open("data/index.yaml"), Loader=Loader),
        "links": load(open("data/links.yaml"), Loader=Loader),
        "maintainers": load(open("data/maintainers.yaml"), Loader=Loader),
        "pages": load(open("data/pages.yaml"), Loader=Loader),
        "platform": load(open("data/platform.yaml"), Loader=Loader),
        "controller_archive": load(open("data/controller_archive.yaml"), Loader=Loader),
        "controller_i18n_links": load(open("data/controller_i18n_links.yaml"), Loader=Loader),
        "controller_translations": load(open("data/controller_translations.yaml"), Loader=Loader),
        "core_translations": load(open("data/core_translations.yaml"), Loader=Loader),
        "users": load(open("data/users.yaml"), Loader=Loader),
    }

buildpath = Path('output')

if buildpath.exists() and buildpath.is_dir():
    shutil.rmtree(buildpath)

if __name__ == "__main__":

    site = Site.make_site()
    site.outpath=buildpath
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)


    shutil.copytree('static', buildpath / 'static')
    sass.compile(dirname=('sass', buildpath / 'static/css'))
