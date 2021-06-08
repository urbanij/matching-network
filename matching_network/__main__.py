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
@click.option('--from', '-f', 'from_', required=True, type=str)
@click.option('--to', '-t', 'to', required=True, type=str)
@click.option('--frequency', '--freq', 'frequency', required=False, type=float)
def cli(from_, to, frequency):
    if ("mS") in from_:
        try:
            from_mS = complex(from_.split()[0])
            from_ = 1/(from_mS * 1e-3)
        except Exception as e:
            print(e)
    else: # assumed ohm if unspecified
        try:
            from_ = complex(from_)
        except ValueError:
            print("Error: Did you mean `mS`?")
            return
        

    if ("mS") in to:
        try:
            to_mS = complex(to.split()[0])
            to = 1/(to_mS * 1e-3)
        except Exception as e:
            print(e)
    else: # assumed ohm if unspecified
        try:
            to = complex(to)
        except ValueError:
            print("Error: Did you mean `mS`?")
            return
        

    
    print(
        mn.L_section_matching(
            input_impedance=from_, 
            output_impedance=to, 
            frequency=frequency
        ).match()
    )

cli()