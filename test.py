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
    print("Test with arg: 'Patrick Böttner'")
    app.main("Patrick Böttner")

    print("Test with arg: 'Heike Bretschner'")
    app.main("Heike Bretschner")

    print("Test with arg: 'Georgi Nikolov'")
    app.main("Georgi Nikolov")

    print("Test with arg: 'Sara Gnauck'")
    app.main("Sara Gnauck")
    

    # test with no arg
    # ERROR will be indicated by a raised exception
    print("\nTest without arg: ")
    app.main()
    

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    test()
