from __future__ import annotations
from abc import abstractmethod
from math import inf, floor, ceil
from typing import Optional, Tuple, Generic, TypeVar, Protocol, Union


class Comparable(Protocol):
    """Protocol for annotating comparable types."""

    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        pass


T = TypeVar("T", bound=Comparable)


class LinkedList(Generic[T]):
    def __init__(self, data: T, next_: Optional[LinkedList[T]] = None) -> None:
        self.data = data
        self.next = next_

    def __repr__(self) -> str:
        try:
            return str(self.data) + (
                ("-" + repr(self.next)) if self.next is not None else ""
            )
        except RecursionError:
            return str(self.data) + (("-" + "...") if self.next is not None else "")

    def contains(self, data: T) -> bool:
        if self.data == data:
            return True
        if self.next is None:
            return False
        return self.next.contains(data)

    def get_last(self) -> LinkedList[T]:
        """Returns the last item in the linked list."""
        cur = self
        # follow links until the end of the list
        while cur.next is not None:
            cur = cur.next
        return cur

    def __len__(self) -> int:
        if self.next is None:
            return 1
        return 1 + len(self.next)

    def split_equal(self) -> Tuple[LinkedList[T], Optional[LinkedList[T]]]:
        """
        Splits a list equally into two parts. Returns a tuple consisting of
        two separated linked lists.

        In case the LinkedList consists of a single item, the second item in
        the tuple will be None.
        In case the LinkedList consists of an uneven number of items (n + 1 +
        n), with n >= 1, the first item in the result tuple will contain the
        uneven element ((n+1), n).
        """
        slow = self
        fast = self
        while True:
            if slow.next is None:
                return (slow, None)
            if fast.next is None or fast.next.next is None:
                front = self
                back = slow.next
                slow.next = None  # split front and back
                return (front, back)

            slow = slow.next
            fast = fast.next.next

    def is_circular(self) -> bool:
        """Determines if a list is circular or not."""
        slow = self
        fast = self
        while True:
            if slow.next is None or fast.next is None or fast.next.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return False
            if slow == fast:
                return True

    def append(self, data: T) -> None:
        """Insert an item at the tail."""
        last = self.get_last()
        last.next = LinkedList(data, None)

    def reverse(self: LinkedList[T]) -> LinkedList[T]:
        """Reverses a given LinkedList by traversing through it once."""
        r: Optional[LinkedList[T]] = None
        p = self
        while p is not None:
            q = p.next
            p.next = r
            r = p
            if q is None:
                break
            p = q
        return r

    def pop(self) -> Tuple[T, Optional[LinkedList[T]]]:
        """Extract and return the first item in the LinkedList."""
        head = self.data
        tail = self.next
        return (head, tail)

    def insert(self, index: int, data: T) -> None:
        if index <= 0:
            raise ValueError("index must be larger than zero")

        cur = self
        i = 0
        while i < index - 1 and cur.next is not None:
            cur = cur.next
            i += 1
        tail = cur.next
        cur.next = LinkedList(data, tail)

    @staticmethod
    def sort(ll: LinkedList[T], method: str = "bubblesort") -> LinkedList[T]:
        """
        Sort the linked list by applying a sorting method.
        By default bubblesort is used.
        """
        if method == "bubblesort":
            return _bubblesort(ll)
        raise NotImplementedError(f"Method '{method}' for sorting is not implemented.")

    def dedupe(self) -> LinkedList[T]:
        p = self
        while p.next is not None:
            q = p.next
            if p.data == q.data:
                if q.next is None:
                    p.next = None
                    break
                else:
                    p.next = q.next
                    q = q.next
            else:
                p = q
        return self

    @staticmethod
    def merge(list1: LinkedList[T], list2: LinkedList[T]) -> LinkedList[T]:
        last = list1.get_last()
        last.next = list2
        return list1

    def is_palindrome(self) -> bool:
        """
        Tests if the LinkedList is a palindrome by splitting the list in equal
        parts, then reverse the second part and compare the items.
        After it has been determined if the list is a palindrome the original
        linked list is restored again.
        """
        part1, part2 = self.split_equal()

        # Exit early if the LinkedList has len 1, which means part2 will be
        # None (see definition of split_equal method).
        if part2 is None:
            return True

        # Reverse the second part so that part1 and part2 can be compared item
        # by item in the chain.
        part2 = LinkedList.reverse(part2)

        p = part1
        q = part2
        result = None
        while True:
            if p.data != q.data:
                result = False
                break
            if p.next is None or q.next is None:
                result = True
                break
            p = p.next
            q = q.next

        # attach reversed part2 list to end of part1, which is now either
        # p (even length) or p.next (uneven length).
        if p.next is not None:
            p = p.next
        p.next = LinkedList.reverse(part2)

        return result


def _bubblesort(ll: LinkedList[T]) -> LinkedList[T]:
    """
    Bubble sort with link exchange.
    See: https://en.wikipedia.org/wiki/Bubble_sort
    """
    start_node = ll  # start node must be variable
    end = None
    while end != start_node:
        r = p = start_node
        while p.next is not None and p.next != end:
            q = p.next
            if p.data > q.data:
                # sort by exchanging references to next items
                p.next = q.next
                q.next = p
                if p != start_node:
                    r.next = q
                else:
                    start_node = q
                p, q = q, p
            # move to next item in chain
            r = p
            assert p.next is not None  # needed for mypy
            p = p.next
        end = p  # ignore rest, because it's already sorted
    return start_node
