#required download punkt, averaged_perceptron_tagger

import nltk
import unittest

def tokenize(sentence):
	return nltk.word_tokenize(sentence)
	
def pos(array):
    return nltk.pos_tag(array)

class TestTokenize(unittest.TestCase):
  def test_tokens(self):
  	sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
  	tokens = tokenize(sentence)
  	self.assertEqual(tokens, ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning', 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.'])

class TestPos(unittest.TestCase):
    def test_do_pos_run(self):
        sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
        pos_tokens = pos(tokenize(sentence))
        self.assertTrue(True)

print("Running Tests")

unittest.main()