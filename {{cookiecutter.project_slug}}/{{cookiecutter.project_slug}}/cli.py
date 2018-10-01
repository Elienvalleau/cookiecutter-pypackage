# -*- coding: utf-8 -*-

"""Console script for {{cookiecutter.project_slug}}."""
{%- if cookiecutter.command_line_interface == 'click' %}
import click
{%- elif cookiecutter.command_line_interface == 'Argparse' %}
import argparse
{%- else %}
import sys
{%- endif %}
{%- if cookiecutter.command_line_interface == 'Click' %}


@click.command()
@click.argument('names', nargs=-1)
def main(names):
    click.echo(repr(names))
{%- elif cookiecutter.command_line_interface == 'Argparse' %}

parser = argparse.ArgumentParser(description='Command description.')
parser.add_argument('names', metavar='NAME', nargs=argparse.ZERO_OR_MORE,
                    help="A name of something.")


def main(args=None):
    args = parser.parse_args(args=args)
    print(args.names)
{%- else %}


def main(argv=sys.argv):
    print(argv)
    return 0
{%- endif %}
