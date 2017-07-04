from ipdb import post_mortem
import click

stringvar = 'Hello World'
another_piece_of_code = 'Lala lalala laalal'

def testfunc(p1, p2):
    return p1 + p2

@click.command()
@click.option('--debug', is_flag=True)
def main(debug):
    try:
        nothing = another_piece_of_code.split()
        testfunc(stringvar, 1) # this should throw the error!
    except:
        if debug:
            post_mortem()
        else:
            raise  #this will just surface the errors

if __name__ == '__main__':
    main()
