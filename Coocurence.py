#required download punkt, averaged_perceptron_tagger

import nltk
import unittest
from nltk.stem.porter import PorterStemmer

def tokenize(sentence):
	return nltk.word_tokenize(sentence)
	
def pos(array):
    return nltk.pos_tag(array)
    
def stem(sentence):
    st = PorterStemmer()
    return st.stem(sentence)
    
def take_all_pair(sentence, space):
    tokens = tokenize(sentence)
    pair = []
    for i in range(0,len(tokens)-(space-1)):
        if(i+space < len(tokens)):
            pair.append([tokens[i],tokens[i+space]])
            
    return pair
        

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
        
class TestStem(unittest.TestCase):
    def test_do_stem_run(self):
        sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
        stem_result = stem(sentence)
        self.assertTrue(True)
        
class TestPair(unittest.TestCase):
    def test_do_pair_work(self):
        sentence = """Hello this is a"""
        pair_result = take_all_pair(sentence, 1)
        self.assertEqual([["Hello","this"],["this","is"],["is","a"]], pair_result)
        
    def test_do_pair_with_2(self):
        sentence = """Hello this is a"""
        pair_result = take_all_pair(sentence, 2)
        self.assertEqual([["Hello","is"],["this","a"]], pair_result)

print("Running Tests")
unittest.main()