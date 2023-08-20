"""
DOCUMENTATION:

"""

import app
import sys


# tests
def test():
    """
    simple smoke test... does it work?
    """

    # test with arg
    print("Test with arg: ")
    app.main("Jan and Rafael")

    # test with no arg
    # ERROR will be indicated by a raised exception
    print("\nTest without arg: ")
    app.main()
    

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    test()
