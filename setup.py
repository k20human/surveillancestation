from setuptools import setup

setup(name='surveillancestation',
      version='0.1',
      description='Synology Surveillance Station 7 API',
      url='http://github.com/k20human/surveillancestation',
      author='k20human',
      author_email='kmat.null@gmail.com',
      license='MIT',
      packages=['surveillancestation'],
      install_requires=[
            'requests',
            'json',
            'logging'
      ],
      zip_safe=False)
