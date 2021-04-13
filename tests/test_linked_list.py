from linked_list import LinkedList
import pytest
import unittest

class TestLinkedList(unittest.TestCase):
    def test_repr_impl(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert repr(ll) == '1-2-3'
        
    def test_repr_for_circular_lists_should_be_finite(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert ll.next is not None
        assert ll.next.next is not None
        ll.next.next.next = ll
        assert repr(ll)[:12] == '1-2-3-1-2-3-'
        assert repr(ll)[-3:] == '...'

    def test_contains_impl(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert ll.contains(1) == True
        assert ll.contains(3) == True
        assert ll.contains(4) == False 

    def test_append_impl(self):
        ll: LinkedList[int] = LinkedList(1)
        assert len(ll) == 1

        ll.append(2)

        assert len(ll) == 2
        assert ll.next is not None
        assert ll.next.data == 2

        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert len(ll) == 3

    def test_is_circular_should_not_return_false_for_noncircular_lists(self):
        ll: LinkedList[int] = LinkedList(1, None)
        assert ll.is_circular() == False

    def test_is_circular_should_return_true_for_circular_lists(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert ll.next is not None
        assert ll.next.next is not None
        ll.next.next.next = ll
        assert ll.is_circular() == True

    def test_split_equal_should_split_in_equal_parts(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2))
        assert repr(ll.split_equal()) == "(1, 2)"

        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5, LinkedList(6))))))
        assert repr(ll.split_equal()) == "(1-2-3, 4-5-6)"

    def test_split_equal_should_split_single_entry(self):
        ll: LinkedList[int] = LinkedList(1)
        assert repr(ll.split_equal()) == "(1, None)"

    def test_split_equal_should_split_odd_entries(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert repr(ll.split_equal()) == "(1-2, 3)"

    def test_pop_impl(self):    
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        (head, tail) = ll.pop()
        assert repr(head) == '1'
        assert repr(tail) == '2-3'

    def test_insert_should_insert_at_position(self):    
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        ll.insert(1, 100)
        assert repr(ll) == "1-100-2-3"
    
    def test_insert_should_insert_at_end_if_pos_is_larger_than_linkedlist(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2))
        ll.insert(100, 3)  # value larger than list size
        assert repr(ll) == '1-2-3'

    def test_merge_impl(self):
        l1: LinkedList[int] = LinkedList(1)
        l2: LinkedList[int] = LinkedList(2)
        assert repr(LinkedList.merge(l1, l2)) == '1-2'

    def test_sort_impl(self):
        ll: LinkedList[int] = LinkedList(3, LinkedList(2, LinkedList(1)))
        assert repr(LinkedList.sort(ll)) == '1-2-3'

        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(1)))
        assert repr(LinkedList.sort(ll)) == '1-1-2'
    
    def test_dedupe_impl(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(1, LinkedList(1)))
        assert repr(LinkedList.dedupe(ll)) == '1'

        ll: LinkedList[int] = LinkedList(2, LinkedList(1, LinkedList(1)))
        assert repr(LinkedList.dedupe(ll)) == '2-1'

        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(2, LinkedList(1))))
        assert repr(LinkedList.dedupe(ll)) == '1-2-1'

    def test_reverse_impl(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3, LinkedList(4))))
        assert repr(ll.reverse()) == '4-3-2-1'

        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert repr(ll.reverse()) == '3-2-1'

        ll: LinkedList[int] = LinkedList(1)
        assert repr(ll.reverse()) == '1'

    def test_palindrome_should_return_true_for_palindroms(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(2, LinkedList(1))))
        assert ll.is_palindrome()
        assert repr(ll) == '1-2-2-1'

        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(1)))
        assert ll.is_palindrome()
        assert repr(ll) == '1-2-1'

    def test_palindrome_should_return_true_for_single_entry_linked_lists(self):
        ll: LinkedList[int] = LinkedList(1)
        assert ll.is_palindrome()
        assert repr(ll) == '1'

    def test_palindrome_should_return_false_if_input_is_no_palindrome(self):
        ll: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert not ll.is_palindrome()
        assert repr(ll) == '1-2-3'
