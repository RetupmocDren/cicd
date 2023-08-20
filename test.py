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
    try:
        # test with arg
        print("Test with arg: ")
        app.main("World")

        # test with no arg
        print("\nTest without arg: ")
        app.main()
    except Exception:
        print(sys.exc_info())
        return 0
    
    return 1

#-------------------------------------------------------------------------------

if __name__ == "__main__":
    test()