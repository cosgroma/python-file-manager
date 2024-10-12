"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -msgt_file_manager` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``sgt_file_manager.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``sgt_file_manager.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

from pathlib import Path
from pprint import pprint

import click
from pygments import formatters
from pygments import highlight
from pygments import lexers

from .core import cmd_scan


@click.command()
@click.argument("directory", type=click.Path(exists=True))
@click.option("--pretty", "-p", is_flag=True)
@click.option("--db-file", "-f", is_flag=False)
def sgt_kb_main(directory: str, pretty: bool, db_file: str = "./output_file.json"):
    """CLI interface kb file scanner"""
    db_file_path = Path(db_file)
    data = cmd_scan(directory, db_file_path)
    if pretty:
        data = highlight(data, lexers.JsonLexer(), formatters.TerminalFormatter())
    else:
        pprint(data)
