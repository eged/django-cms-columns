# encoding=utf8
from setuptools import setup, find_packages

setup(
    name = 'django-cms-columns',
    version = '0.1a1',
    license = 'BSD',
    description = 'Variable column support for django-cms plugins',
    author = u'Samuel Lüscher',
    author_email = 'philomat@popkultur.net',
    url = 'http://github.com/philomat/django-cms-columns',
    packages = find_packages(),
    package_data = {
        'cms_columns': [
            'templates/cms_columns/*.html',    
            'templates/cms_columns/*.txt',
            'locale/*/LC_MESSAGES/*',
            ],
    },
    zip_safe=False,
)