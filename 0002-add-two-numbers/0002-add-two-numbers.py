# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getStringNumber(l: ListNode) -> str:
    if l.next is None:
        return str(l.val)
    else:
        return getStringNumber(l.next) + str(l.val)

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = getStringNumber(l1), getStringNumber(l2)
        n3 = int(n1) + int(n2)

        stack = []
        for a in str(n3):
            stack.append(int(a))

        last = ListNode(stack.pop(0))
        while stack != []:
            last = ListNode(stack.pop(0), last)
        
        return last
        