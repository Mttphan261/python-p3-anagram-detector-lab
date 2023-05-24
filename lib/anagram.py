# your code goes here!

class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list):
        sorted_self = sorted([letter for letter in self.word])
        anagram_list = []

        for each in list:
            if sorted_self == sorted([letter for letter in each]):
                anagram_list.append(each)
                
        return anagram_list


