from data_structures import Stack
import pytest
import unittest


class TestStack(unittest.TestCase):
    def test_empty_stack(self):
        stack = Stack()
        assert stack.is_empty()

    def test_push_new_entry(self):
        stack = Stack()
        stack.push(1)

        assert not stack.is_empty()
        assert stack.top() == 1

    def test_size_of_stack(self):
        stack = Stack()
        stack.push(1)
        assert stack.size() == 1
        stack.push(2)
        assert stack.size() == 2

    def test_pop_of_empty_stack(self):
        stack = Stack()
        val = stack.pop()
        assert val is None
        assert stack.size() == 0

    def test_pop_of_filled_stack(self):
        stack = Stack()

        stack.push(1)
        assert stack.size() == 1

        val = stack.pop()
        assert val == 1
        assert stack.size() == 0

    def test_pop_of_filled_stack_long(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.size() == 3

        val = stack.pop()
        assert val == 3
        assert stack.size() == 2

    def test_pop_should_remove(self):
        stack = Stack()
        # first push two items, ...
        stack.push(1)
        stack.push(2)
        # ... then remove last item ...
        stack.pop()
        # ... and make sure that reference to popped entry is removed
        assert stack._linked_list.get_last().next is None
        assert stack.top() == stack._linked_list.get_last().data