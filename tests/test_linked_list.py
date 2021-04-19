from data_structures import LinkedList
import pytest
import unittest


class TestLinkedList(unittest.TestCase):
    def test_repr_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert repr(list1) == "1-2-3"

    def test_repr_for_circular_lists_should_be_finite(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert list1.next is not None
        assert list1.next.next is not None
        list1.next.next.next = list1
        assert repr(list1)[:12] == "1-2-3-1-2-3-"
        assert repr(list1)[-3:] == "..."

    def test_contains_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert list1.contains(1) == True
        assert list1.contains(3) == True
        assert list1.contains(4) == False

    def test_append_impl(self) -> None:
        ll = LinkedList(1)
        assert len(ll) == 1

        ll.append(2)

        assert len(ll) == 2
        assert ll.next is not None
        assert ll.next.data == 2

        list2: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert len(list2) == 3

    def test_is_circular_should_not_return_false_for_noncircular_lists(self) -> None:
        ll = LinkedList(1, None)
        assert ll.is_circular() == False

    def test_is_circular_should_return_true_for_circular_lists(self):
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert list1.next is not None
        assert list1.next.next is not None
        list1.next.next.next = list1
        assert list1.is_circular() == True

    def test_split_equal_should_split_in_equal_parts(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2))
        assert repr(list1.split_equal()) == "(1, 2)"

        list2: LinkedList[int] = LinkedList(
            1, LinkedList(2, LinkedList(3, LinkedList(4, LinkedList(5, LinkedList(6)))))
        )
        assert repr(list2.split_equal()) == "(1-2-3, 4-5-6)"

    def test_split_equal_should_split_single_entry(self) -> None:
        ll = LinkedList(1)
        assert repr(ll.split_equal()) == "(1, None)"

    def test_split_equal_should_split_odd_entries(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert repr(list1.split_equal()) == "(1-2, 3)"

    def test_pop_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        (head, tail) = list1.pop()
        assert repr(head) == "1"
        assert repr(tail) == "2-3"

    def test_insert_should_insert_at_position(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        list1.insert(1, 100)
        assert repr(list1) == "1-100-2-3"

    def test_insert_should_insert_at_end_if_pos_is_larger_than_linkedlist(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(2))
        list1.insert(100, 3)  # value larger than list size
        assert repr(list1) == "1-2-3"

    def test_merge_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(1)
        list2: LinkedList[int] = LinkedList(2)
        assert repr(LinkedList.merge(list1, list2)) == "1-2"

    def test_sort_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(3, LinkedList(2, LinkedList(1)))
        assert repr(LinkedList.sort(list1)) == "1-2-3"

        list2: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(1)))
        assert repr(LinkedList.sort(list2)) == "1-1-2"

    def test_dedupe_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(1, LinkedList(1, LinkedList(1)))
        assert repr(LinkedList.dedupe(list1)) == "1"

        list2: LinkedList[int] = LinkedList(2, LinkedList(1, LinkedList(1)))
        assert repr(LinkedList.dedupe(list2)) == "2-1"

        list3: LinkedList[int] = LinkedList(
            1, LinkedList(2, LinkedList(2, LinkedList(1)))
        )
        assert repr(LinkedList.dedupe(list3)) == "1-2-1"

    def test_reverse_impl(self) -> None:
        list1: LinkedList[int] = LinkedList(
            1, LinkedList(2, LinkedList(3, LinkedList(4)))
        )
        assert repr(list1.reverse()) == "4-3-2-1"

        list2: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert repr(list2.reverse()) == "3-2-1"

        list3: LinkedList[int] = LinkedList(1)
        assert repr(list3.reverse()) == "1"

    def test_palindrome_should_return_true_for_palindroms(self) -> None:
        list1: LinkedList[int] = LinkedList(
            1, LinkedList(2, LinkedList(2, LinkedList(1)))
        )
        assert list1.is_palindrome()
        assert repr(list1) == "1-2-2-1"

        list2: LinkedList[int] = LinkedList(1, LinkedList(2, LinkedList(1)))
        assert list2.is_palindrome()
        assert repr(list2) == "1-2-1"

    def test_palindrome_should_return_true_for_single_entry_linked_lists(self) -> None:
        list1: LinkedList[int] = LinkedList(1)
        assert list1.is_palindrome()
        assert repr(list1) == "1"

    def test_palindrome_should_return_false_if_input_is_no_palindrome(self) -> None:
        list1 = LinkedList(1, LinkedList(2, LinkedList(3)))
        assert not list1.is_palindrome()
        assert repr(list1) == "1-2-3"
