# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            y = x
            m = 1
            while(y//10>0):
                m *= 10
                y = y//10
            i = 1
            while(m>=10 and x>=10):
                if (x//m)%10 != (x%(10*i))//i:
                    return False
                print(m)
                m //= 10
                i *= 10
            return True
        else:
            return False
