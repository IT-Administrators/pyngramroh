"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir
# Import Monogram class of pyngramroh module.
from src.pyngramroh import ngram as ng

importdir()

class TestPyngramrohNGram_MonoGram(unittest.TestCase):
    """Test Monogram class of pyngramroh module."""
    
    def setUp(self) -> None:
        self.testlist = ["This is a demonstration string."]
        self.reslistn1 = [["This"],["is"],["a"],["demonstration"],["string"]]
        self.reslistn2 = [["This","is"],["is","a"],["a","demonstration"],["demonstration","string"]]
        self.reslistn3 = [["This","is", "a"],["is","a","demonstration"],["a","demonstration","string"]]
        self.reslistn4 = [["This","is","a","demonstration"],["is","a","demonstration","string"]]
        self.reslistn5 = [["This","is","a","demonstration","string"]]

    # Test monogram creation.
    def test_pyngramroh_monogram(self):
        monog = ng.NGram(self.testlist[0])
        self.assertEqual(monog.generate_ngram(), self.reslistn1)

    # Test bigram creation.
    def test_pyngramroh_bigram(self):
        big = ng.NGram(self.testlist[0],2)
        self.assertEqual(big.generate_ngram(), self.reslistn2)

        # Test bigram creation.
    def test_pyngramroh_trigram(self):
        trig = ng.NGram(self.testlist[0],3)
        self.assertEqual(trig.generate_ngram(), self.reslistn3)
    
    # Test multigram creation.
    def test_pyngramroh_multigram(self):
        multig = ng.NGram(self.testlist[0],4)
        self.assertEqual(multig.generate_ngram(), self.reslistn4)
        multig = ng.NGram(self.testlist[0],5)
        self.assertEqual(multig.generate_ngram(), self.reslistn5)


if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()