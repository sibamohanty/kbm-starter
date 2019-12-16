"""Main entry point
"""
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession
import sqlalchemy as sa


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    sa.orm.configure_mappers()
    # Session = sessionmaker(bind=engine)

    DBSession.configure(bind=engine)
    # session = Session()

    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("kbm.views")
    return config.make_wsgi_app()

