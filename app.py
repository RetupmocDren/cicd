"""
DOCUMENTATION:

"""

import sys

#-------------------------------------------------------------------------------

def main( *args, **kwargs):
    """
    only the first arg is used 
    """

    name = args[0]

# FIX: for no given parameters
#    try:
#        name = args[0][0]
#    except IndexError:
#        name = "world"

    print("HELLO, %s" %name)

    return 0

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        # only args will be processed
        main(sys.argv[1])
    except IndexError:
        # if no arg is given
        main()