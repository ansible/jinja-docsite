from staticjinja import Site
from yaml import Loader, load


def data():
    return {
        "base": load(open("data/base.yaml"), Loader=Loader),
        "links": load(open("data/links.yaml"), Loader=Loader)
    }

if __name__ == "__main__":
    site = Site.make_site()
    site.contexts=[(".*.html", data)]
    # disable automatic reloading
    site.render(use_reloader=False)