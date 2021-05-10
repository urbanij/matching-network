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
import matching_network as mn


@click.command()
# @click.argument('keyword', required=False)
@click.option('--from', '-f', 'from_', required=True, type=complex)
@click.option('--to', '-t', 'to', required=True, type=complex)
@click.option('--frequency', '--freq', 'frequency', required=False, type=float)
def cli(from_, to, frequency):
    print(
        mn.L_section_matching(
            input_impedance=from_, 
            output_impedance=to, 
            frequency=frequency
        ).match()
    )

cli()