from setuptools import setup

def readme():
    with open('readme.md') as f:
        return f.read()

setup(
    name='gt-py',
    packages=['gt-py'],
    install_requires=['unittest2==1.1.0', 'requests==2.9.1'],
    version='1.0',
    license='MIT',
    description='Python library for GovTrack.us API',
    author='Peixian Wang',
    author_email='peixian@driftingicebergs.com',
    url='https://github.com/peixian/gt-py',
    download_url='https://github.com/peixian/gt-py/archive/1.0.tar.gz',
    keywords=['api', 'python', 'govtrack', 'gt'],
    classifiers=[],
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
)
