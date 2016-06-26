from setuptools import setup

setup(
    name='gt-py',
    packages=['govtrack'],
    install_requires=['unittest2==1.1.0', 'requests==2.9.1'],
    version='0.1',
    description='Python library for GovTrack.us API',
    author='Peixian Wang',
    author_email='peixian@driftingicebergs.com',
    url='https://github.com/peixian/gt-py',
    download_url='',
    keywords=['api', 'python', 'govtrack', 'gt'],
    classifiers=[],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
)
