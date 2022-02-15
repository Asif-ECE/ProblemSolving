# Given a string s, reverse the order of characters in each word within a sentence while
# still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:
        myList = s.split()
        l = len(myList)-1
        for i in range(l):
            string = myList.pop(0)
            myList.insert(l,string)
            l -= 1
        myString = " ".join(myList)
            
        return myString[::-1]
