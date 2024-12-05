# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Definition for singly-linked list.

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val):
        new_node = ListNode(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.head is None:
            return "Empty List"
        temp = self.head  # top
        # while temp.next is not None:
        #     temp = temp.next
        #     print(temp.val)
        for _ in range(self.length):
            print(temp.val)
            temp = temp.next

    def append_values(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        if index not in range(self.length):
            return "Unbound Index"
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        if index not in range(self.length):
            return "Unbound Index"
        temp = self.get(index)
        if temp:
            temp.val = value
            return True
        return False

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.


class Solution:
    def addTwoNumbers(self, l1, l2):
        length_1 = l1.length

        summated_dict = {}  # Linked
        for index in range(length_1):
            temp_1 = ll1.get(index)
            temp_2 = ll2.get(index)
            summated_dict[index] = temp_1.val + temp_2.val

        result_ll = LinkedList(0)
        for index in range(len(summated_dict)):
            result_ll.append_values(summated_dict[index])

        for index in range(result_ll.length):
            list_node_value = result_ll.get(index)
            if list_node_value.val >= 10:
                # If the current node has value greated than 10, subtract it by 10
                list_node_value.val = list_node_value.val - 10
                # get the index of the next node, and then add + 1 to that node's value and assign it back
                next_node = result_ll.get(index+1)
                final_value = next_node.val + 1
                result_ll.set(index+1, final_value)

        return result_ll


l1 = [2, 4, 3]
l2 = [5, 6, 4]
ll1 = LinkedList(2)
ll1.append_values(4)
ll1.append_values(3)
ll2 = LinkedList(5)
ll2.append_values(6)
ll2.append_values(4)


sol = Solution()
output = sol.addTwoNumbers(ll1, ll2)
print("first_list")
ll1.print_list()
print("second_list")
ll2.print_list()
print("list is getting printed here!")
output.print_list()
