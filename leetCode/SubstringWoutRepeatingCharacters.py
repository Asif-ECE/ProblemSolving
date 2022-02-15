# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inputString = s
        length = len(inputString)
        
        outputString = ""
        count = 0
        
        for i in range(length):
            if inputString[i] not in outputString:
                outputString += inputString[i]
            elif inputString[i] == inputString[i-1]:
                if len(outputString)>count:
                    count = len(outputString)
                outputString = inputString[i]
            else:
                if len(outputString)>count:
                    count = len(outputString)
                x = outputString.index(inputString[i])
                outputString = outputString[x+1:]+inputString[i]
        
        if len(outputString)>count:
            count = len(outputString)
        return count
