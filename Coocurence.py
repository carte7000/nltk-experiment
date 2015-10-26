#required download punkt, averaged_perceptron_tagger

import nltk
import unittest
import math
import codecs
from nltk.stem.porter import PorterStemmer

def tokenize(sentence):
    se = sentence#.encode("UTF-8")
    return nltk.word_tokenize(se)
	
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
    
def take_all_pair_array(tagged_array, space):
    pair = []
    for i in range(0,len(tagged_array)-(space-1)):
        if(i+space < len(tagged_array)):
            pair.append([tagged_array[i],tagged_array[i+space]])
            
    return pair
        
def count_word(word_array):
    word_dict = dict()
    for word in word_array:
        if word not in word_dict:
            word_dict[word] = 0
            
        word_dict[word]+=1
    
    return word_dict
    
        
def count_pair(pair_array):
    pair_dict = dict()
    for pair in pair_array:
        if tuple(pair) not in pair_dict:
            pair_dict[tuple(pair)] = 0
            
        pair_dict[tuple(pair)]+=1
    
    return pair_dict
    
def filter_tag(array, allowedPairTag):
    pos_result = pos(array)
    pair_array = take_all_pair_array(pos_result, 1)
    pair_dict = count_pair(pair_array)
    
    result = dict()
    for key, value in pair_dict.iteritems():
        if extractPos(list(key)) in allowedPairTag:
            rekey = [list(list(key)[0])[0],list(list(key)[1])[0]]
            result[tuple(rekey)] = value
    
    return result

def extractPos(tagged_array):
    result = []
    for tag in tagged_array:
        result.append(tag[1])
        
    return result
    
def tTest(wordCountDict, pairCountDict, numberOfWords):
    numberOfPairs = numberOfWords-1
    coocurences = dict()
    for key, value in pairCountDict.iteritems():
        pPair = float(value)/numberOfPairs
        pMu = (wordCountDict[list(key)[0]]/numberOfWords)*(wordCountDict[list(key)[1]]/numberOfWords)
        tTest = (pPair-pMu)/(math.sqrt(pPair/numberOfPairs))
        coocurences[key]=tTest
    
    return coocurences
    
def MI(wordCountDict, pairCountDict, numberOfWords):
    numberOfPairs = numberOfWords-1
    coocurences = dict()
    for key, value in pairCountDict.iteritems():
        pPair = float(value)/numberOfPairs
        pMu = (wordCountDict[list(key)[0]]/numberOfWords)*(wordCountDict[list(key)[1]]/numberOfWords)
        mi = math.log(pPair/pMu)
        coocurences[key]=mi
        
    return coocurences
    
    
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
        
class TestCount(unittest.TestCase):
    def test_do_count_pair_work(self):
        count_result = count_pair([["a","a"],["a","a"],["b","a"]])
        self.assertTrue(count_result[tuple(["a","a"])]==2)
        self.assertTrue(count_result[tuple(["b","a"])]==1)
        
class TestFilter(unittest.TestCase):
    def test_do_filter_pair_work(self):
        filter_result = filter_tag(tokenize("they refuse to"), [["PRP","VBP"]])
        #filter_result = filter_tag(count_pair([["they","refuse"],["refuse","to"]]), [["PRP","VBP"]])
        self.assertTrue(tuple(["they","refuse"]) in filter_result)
        self.assertFalse(tuple(["refuse","to"]) in filter_result)
        
class TesttTest(unittest.TestCase):
    def test_do_tTest_run(self):
        test = tokenize("they refuse to")
        wordCountDict = count_word(test)
        pair = take_all_pair_array(test, 1)
        pairCountDict = count_pair(pair)
        tTest(wordCountDict, pairCountDict, 3)

#print("Running Tests")
#unittest.main()

file = codecs.open('file_collection_cc_punct_line.txt', 'r', encoding='utf-8')

test = tokenize(file.read())

wordCountDict = count_word(test)
pairCountDict = count_pair(take_all_pair(test,1))

tTest(wordCountDict, pairCountDict, len(test))