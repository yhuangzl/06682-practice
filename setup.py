from setuptools import setup

setup(name='s23openalex',
      version='0.0.1',
      description='s23 openalex',
      maintainer='Yu-Hsun Huang',
      maintainer_email='yuhsunh@andrew.cmu.edu',
      license='MIT',
      packages=['s23openalex'],
      entry_points={'console_scripts': ['oa = s23openalex.main:main']}, # create a terminal command "oa"
      long_description='''A long
      multiline description.''')
