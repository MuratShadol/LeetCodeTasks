"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node
