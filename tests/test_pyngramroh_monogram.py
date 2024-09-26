"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir
# Import Monogram class of pyngramroh module.
from src.pyngramroh import monogram as mg

importdir()

testlist= ["This is demonstration string."]

class TestPyngramrohMonoGram(unittest.TestCase):
    """Test Monogram class of pyngramroh module."""
    def setUp(self) -> None:
        self.testlist = testlist
    
    # Test the monogram part of the pyngramroh module.
    ng = mg.MonoGram(testlist[0])
    print(ng.string)

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()