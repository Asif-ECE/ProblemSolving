# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        inputList = head
        middle = head
        l = 1
        while True:
            if inputList.next == None:
                return middle
            inputList = inputList.next
            l += 1
            if l%2 == 0:
                middle = middle.next

#Most optimal solution
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head
        fast = head
        
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
                
        return slow
                