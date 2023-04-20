import click
from .works import Works


@click.command(help='OpenAlex Institutions')
@click.argument('query', nargs=-1)
def main(query):
    w = Works(query[0])
    w.bibtex
