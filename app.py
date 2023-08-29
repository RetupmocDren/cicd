"""
DOCUMENTATION:

"""

import sys

#-------------------------------------------------------------------------------

def main( *args, **kwargs):
    """
    only the first arg is used 
    """
    # BUG: causes IndexError when no arg given
    #name = args[0]

    # FIX: for no given parameters
    try:
        name = args[0]
    except IndexError:
        name = "World"

    print("HELLO, %s" % name)

    return 0

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        # only 1st arg will be processed
        main(sys.argv[1])
    except IndexError:
        # if no arg is given
        main()
