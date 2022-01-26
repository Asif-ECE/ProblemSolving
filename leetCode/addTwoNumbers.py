# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def findNum(listNode):
            if listNode.next != None:
                value = findNum(listNode.next)*10 + listNode.val
            else:
                value = listNode.val
            return value  

        sum = findNum(l1) + findNum(l2)
        
        retList = ListNode()
        
        def constNode(listNode, sums):
            listNode.val = sums%10
            if sums//10 > 0:
                listNode.next = ListNode()
                sums//=10
                constNode(listNode.next,sums)
            return listNode
        return constNode(retList, sum)
