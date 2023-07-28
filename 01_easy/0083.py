# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,1,2]
# Output: [1,2]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # Current Node = Head
        curr = head
        # While Current Node is not null:
        while curr:
            # While node after current isn't null and the value
            # of the current node is equal to the value to the next,
            # point to the next node to check if the value is the same
            # there as well.
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            # Since the value of the next node isnt equal to current,
            # change the current node to the next node.
            curr = curr.next
        # Return the head, not current, because current will end in null.
        return head
