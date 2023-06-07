# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


class Solution(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()  # Dummy node to simplify the code
        current = dummy  # Pointer to the current node in the result list
        carry = 0  # Carry variable

        while l1 or l2 or carry:
            # Get the values of the current nodes (0 if no more nodes)
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum of the current nodes' values and the carry
            total = x + y + carry

            # Update the carry and create a new node for the digit value
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move to the next nodes in both lists if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            # Move to the next node in the result list
            current = current.next

        return dummy.next  # Return the result list (excluding the dummy node)
