# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

list1 = ListNode()
list1.val = 1
list1.next = ListNode()
list1.next.val = 4
list1.next.next = ListNode()
list1.next.next.val = 5

def mergeKLists(lists):
    
    def findAllValues(listNode, finalNode):
        if finalNode.next != None:
            #print(finalNode.val)
            findAllValues(listNode, finalNode.next)
            
        if finalNode.val != 0:
            print(finalNode.val)
            finalNode.next = ListNode()
            findAllValues(listNode, finalNode.next)
            
        finalNode.val = listNode.val
        
        if listNode.next != None:
            finalNode.next = ListNode()
            findAllValues(listNode.next, finalNode.next)
        
    outputNode = ListNode()

    findAllValues(lists[0], outputNode)
    #findAllValues(lists[1], outputNode)
    
    return outputNode
    
x = mergeKLists(list1)
print(x.val)
