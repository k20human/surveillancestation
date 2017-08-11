from setuptools import setup

setup(name='surveillance-station',
      version='0.1',
      description='Synology Surveillance Station 7 API',
      url='http://github.com/k20human/surveillance-station',
      author='k20human',
      author_email='kmat.null@gmail.com',
      license='MIT',
      packages=['surveillance-station'],
      install_requires=[
            'hurry.filesize',
            'requests',
      ],
      zip_safe=False)
