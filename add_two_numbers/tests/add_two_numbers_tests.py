import unittest

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper method to compare two linked lists
    def __eq__(self, other):
        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next
        return self is None and other is None

    # Helper method to create a linked list from a list of values
    @staticmethod
    def from_list(values):
        dummyHead = ListNode(0)
        current = dummyHead
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummyHead.next

    # Helper method to convert a linked list to a list of values
    def to_list(self):
        values = []
        current = self
        while current:
            values.append(current.val)
            current = current.next
        return values


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        l1 = ListNode.from_list([2, 4, 3])  # Represents the number 342
        l2 = ListNode.from_list([5, 6, 4])  # Represents the number 465
        expected = ListNode.from_list([7, 0, 8])  # Represents the number 807
        self.assertEqual(self.solution.addTwoNumbers(l1, l2), expected)

    def test_carry_over(self):
        l1 = ListNode.from_list([9, 9, 9])  # Represents the number 999
        l2 = ListNode.from_list([1])        # Represents the number 1
        # Represents the number 1000
        expected = ListNode.from_list([0, 0, 0, 1])
        self.assertEqual(self.solution.addTwoNumbers(l1, l2), expected)

    def test_different_lengths(self):
        l1 = ListNode.from_list([1, 8])  # Represents the number 81
        l2 = ListNode.from_list([0])     # Represents the number 0
        expected = ListNode.from_list([1, 8])  # Represents the number 81
        self.assertEqual(self.solution.addTwoNumbers(l1, l2), expected)

    def test_zero_case(self):
        l1 = ListNode.from_list([0])  # Represents the number 0
        l2 = ListNode.from_list([0])  # Represents the number 0
        expected = ListNode.from_list([0])  # Represents the number 0
        self.assertEqual(self.solution.addTwoNumbers(l1, l2), expected)

    def test_large_numbers(self):
        # Represents the number 9999999
        l1 = ListNode.from_list([9, 9, 9, 9, 9, 9, 9])
        # Represents the number 9999
        l2 = ListNode.from_list([9, 9, 9, 9])
        expected = ListNode.from_list(
            [8, 9, 9, 9, 0, 0, 0, 1])  # Represents 10009998
        self.assertEqual(self.solution.addTwoNumbers(l1, l2), expected)


if __name__ == "__main__":
    unittest.main()
