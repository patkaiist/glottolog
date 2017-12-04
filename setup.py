from setuptools import setup, find_packages

setup(
    name='pyglottolog',
    version='2.0.0.dev0',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    description='python package for glottolog data curation',
    keywords='data linguistics',
    license='',
    url='https://github.com/clld/glottolog',
    packages=find_packages(),
    platforms='any',
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['glottolog=pyglottolog.__main__:main'],
    },
    install_requires=[
        'six>=1.9',
        'clldutils>=1.9.1',
        'pybtex>=0.20',
        'latexcodec',
        'unidecode',
        'whoosh',
        'attrs',
        'pycountry>=17.01.08',
        'termcolor',
        'newick',
        'markdown',
        'bs4',
        'requests',
    ],
    extras_require={
        'test': ['mock>=2', 'pytest>=3.3', 'pytest-mock', 'pytest-cov'],
    },
    long_description='',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
