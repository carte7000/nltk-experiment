import nltk
import unittest

def tokenize(sentence):
	return nltk.word_tokenize(sentence)

class TestTokenize(unittest.TestCase):
  def test_tokens(self):
  	sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
  	tokens = tokenize(sentence)
  	self.assertEqual(tokens, ['At', 'eight', "o'clock", 'on', 'Thursday', 'morning', 'Arthur', 'did', "n't", 'feel', 'very', 'good', '.'])


print("Running Tests")

unittest.main()