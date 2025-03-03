"""
Pyngramroh.ngram

Create an ngram of the provided string.

Usage:
    from pyngramroh import ngram as ng
    ngram = ng.NGram("This is a demo string.", 2)
    print(ngram.generate_ngram())

Returns:
    [['This', 'is'], ['is', 'demonstration'], ['demonstration', 'string']]

Author: IT-Administrators

License: MIT
"""

import string

class NGram:
    """NGram class."""

    def __init__(self, source:str, ngramcount = 1):
        self.source = source
        self.ngramcount = ngramcount

    def generate_ngram(self):
        """
        Generate ngrams of the specified text using the ngramcount. 
        The ngramcount is the number of words which will be grouped together.
        The result is a list of lists. 
        
        Usage:
            ngram = ng.NGram("This is a demonstration string.")
            print(ngram.generate_ngram(words, 2))
            print(ngram.generate_ngram(words, 3))
            print(ngram.generate_ngram(words, 4))
        
        Return:
            [['This', 'is'], ['is', 'a'], ['a', 'demo'], ['demo', 'string']]
            [['This', 'is', 'a'], ['is', 'a', 'demo'], ['a', 'demo', 'string']]
            [['This', 'is', 'a', 'demo'], ['is', 'a', 'demo', 'string']]
        
        Author: IT-Administrators
        
        License: MIT
        """

        # Result should be [[list1],[list2],[list3]]
        # Result list.
        ngramr = []
        # Sublists.
        ngramg = []
        counter = 0
        
        # Create list of words to process.
        self.words = self._split_string_to_words()

        while counter < len(self._split_string_to_words()):
            # Append word to sublist.
            ngramg.append(self.words[counter])
            if len(ngramg) == self.ngramcount:
                # Append sublist to result list.
                ngramr.append(ngramg)
                # Remove first word from sublist.
                ngramg = ngramg[1:]
            counter += 1

        return ngramr
    
    def _split_string_to_words(self):
        """
        Split string into words. This function is only meant to be a helper function.
        
        Usage:
            teststring = "This is a demo string."
            print(_split_string_to_words(teststring))
        
        Return:
            ['This', 'is', 'a', 'demo', 'string.']
        
        Author: IT-Administrators
        
        License: MIT
        """
        # Remove punctuation than split to words.
        return self._remove_punctuation().split(' ')

    
    def _remove_punctuation(self):
        """
        Remove every punctuation character in specified string.
        
        This function is a helpfer function. Don't import it.

        Usage:
            print(_remove_punctuation("Test."))
        
        Result:
            Test

        Author: IT-Administrators
        
        License: MIT
        """
        # Remove punctutation from source string.
        return self.source.translate(str.maketrans('', '', string.punctuation))  