import click

import pyqt5toolsbuild.utils


@click.group()
def cli():
    pass


@cli.command()
@click.option('--version')
@click.option('--levels', type=int)
@click.option('--remove-dots', is_flag=True)
def exact(version, levels, remove_dots):
    version = pyqt5toolsbuild.utils.Version.from_string(version)

    s = str(version.exactly(levels=levels))

    if remove_dots:
        s = s.replace('.', '')

    print(s)


@cli.command()
@click.option('--version')
def qt(version):
    version = pyqt5toolsbuild.utils.Version.from_string(version)

    print(pyqt5toolsbuild.utils.pyqt_to_qt_version(version))
