from setuptools import setup

setup(
    name='iscconf',
    description="Parser for ISC configuration files.",
    author="Radomir Dopieralski",
    author_email="devel@sheep.art.pl",
    long_description="""
Parser for ISC configuration files, such as ``dhcpd.conf`` or ``named.conf``.
    """,
    version='1.0.2',
    license='GNU',
    url='https://github.com/markraub/iscconf',
    keywords='isc parser config configuration',
    packages=['iscconf'],
    install_requires=['ply'],
    platforms='any',
)
