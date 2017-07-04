from ipdb import launch_ipdb_on_exception
import click

stringvar = 'Hello World'
another_piece_of_code = 'Lala lalala laalal'

def testfunc(p1, p2):
    return p1 + p2


def main():
    nothing = another_piece_of_code.split()
    testfunc(stringvar, 1) # this should throw the error!


# This function runs everything with debugger if you supply the debug flag
#  Why do you want to do this?  because you don't ant the program to hang
#  on a shell if this is running in a production environment
@click.command()
@click.option('--debug', is_flag=True)
def conitional_debug(debug):
    if debug:
        with launch_ipdb_on_exception():
            main()
    else:
        main()

if __name__ == '__main__':
    conitional_debug()
