try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(name='agenda',
      version='1.2.0',
      description="",
      long_description="",
      classifiers=[],
      keywords='',
      author='Mathieu Leduc-Hamel',
      author_email="marrakis@gmail.com",
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'babel',
          'bumpversion',
          'django==1.6.5',
          'django-recaptcha',
          'reindent',
          'requests',
          'simplejson',
          'South',
          'twitter',
          'unidecode',
          'vobject',
          'werkzeug'
      ],
      entry_points={
          'django.apps': [
              'agenda = agenda'
          ],
          'console_scripts': [
              'debug = agenda.command:debug'
          ],
      },
  )
