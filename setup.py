import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
    'psycopg2',
    'pyramid',
    'sqlalchemy',
    'SQLAlchemy-Searchable',
    'pyramid_tm',
    'zope.sqlalchemy',
    'cornice',
    'waitress',
    'pytest',
    'webtest',
    'requests'
]

setup(name='kbm',
      version=0.1,
      description='kbm-cornice',
      # long_description=README,
      install_requires=requires,
      keywords="web services",
      author='siba mphanty',
      author_email='mohanty.siba@gmail.com',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points="""\
      [paste.app_factory]
      main=kbm:main
      
      """,
      paster_plugins=['pyramid'])
