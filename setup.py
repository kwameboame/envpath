from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='envpath',
      version='0.1',
      description='Utility for saving and retrieving your development environments and paths.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='http://github.com/kwameboame/envpath',
      author='Sosthenes Kwame Boame',
      author_email='kwame.boame@live.com',
      keywords="'environment', 'virtualenv', 'envpath', 'python'",
      install_requires=[
          'virtualenv',
          'argparse',
      ],
      entry_points={
        'console_scripts': ['envpath=source.cli:main'],
      },
      license='MIT',
      packages=['source'],
      zip_safe=False)
