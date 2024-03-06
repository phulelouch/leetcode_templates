
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()

#Reverse Link list https://leetcode.com/problems/reverse-linked-list/
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head
        #print(next_node)
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list

#mergeTwoLists https://leetcode.com/problems/merge-two-sorted-lists/
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
      
        head = ListNode(0)
        current = head
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
       
        return head.next


# Find the middle of a linked list with two pointers.
# Time: O(n), Space: O(1)
def middleOfList(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Determine if the linked list contains a cycle.
# Time: O(n), Space: O(1)
def hasCycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Determine if the linked list contains a cycle and
# return the beginning of the cycle, otherwise return null.
# Time: O(n), Space: O(1)
def cycleStart(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return None
    
    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow


# 2130. Maximum Twin Sum of a Linked List
#https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find the middle
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        
        #Reversed the link list at the middle
        new_list = None
        current = slow
        
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node

        #Calculate the max_val
        x = head
        y = new_list
        max_val = 0
        while y:
            total = x.val + y.val
            max_val = max(max_val, total)
            y=y.next
            x=x.next

        return max_val

       
        
