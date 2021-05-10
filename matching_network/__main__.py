# import sys
# import click

# @click.group()
# @click.version_option("0.1.1")
# def main():
#     """A Lumped Parameters LC matching networks CLI solver.

# urbanij.github.io/projects/matching_networks/

# urbanij.github.io/syRF
# """
#     print("Hye")
#     pass


import click

@click.command()
# @click.argument('keyword', required=False)
@click.option('--from', '-f', 'from_', required=True, type=complex)
@click.option('--to', '-t', 'to_', required=True, type=complex)
def match_(from_, to_):
    click.echo('from %s to %s' % (from_, to_))

match_()