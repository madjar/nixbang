from setuptools import setup


setup(
    name='nixbang',
    version='0.1.0',
    description='A special shebang to run scripts in a nix-shell',
    long_description=open('README.rst').read(),
    author='Georges Dubus',
    author_email='georges.dubus@gmail.com',
    url='https://github.com/madjar/nixbang',
    license="BSD",
    scripts=['nixbang'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
