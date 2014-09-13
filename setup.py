"""Setup of the plugin ckanex-widgets"""
from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-widgets',
    version=version,
    description="""This is a CKAN extension to create embedabble
      responsive widgets in other sites""",
    long_description='''
    ''',
    classifiers=[],
    keywords='',
    author='Noe Dominguez Porras & Miguel Angel Gordian',
    author_email='datamx@codeandomexico.org',
    url='http://codeandomexico.org',
    license='AGPL 3.0',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.widgets'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        ckanext-widgets=ckanext.plugin:WidgetsPlugin
        widgets_controller=ckanext.widgets.controller:WidgetsController
    ''',
)
