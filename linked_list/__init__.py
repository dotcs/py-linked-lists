from __future__ import annotations
from typing import Optional, Tuple, Generic, TypeVar
from math import inf

T = TypeVar('T')

class LinkedList(Generic[T]):
    def __init__(self, data, next_=None) -> None:
        self.data: T = data
        self.next: Optional[LinkedList[T]] = next_
    
    def __repr__(self) -> str:
        try:
            return str(self.data) + (('-' + repr(self.next)) if self.next is not None else '')
        except RecursionError:
            return str(self.data) + (('-' + '...') if self.next is not None else '')

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

    def split_equal(self) -> Tuple[LinkedList, Optional[LinkedList]]:
        """Splits a list equally into two parts. Returns a tuple."""
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

    def reverse(self) -> LinkedList[T]:
        pass

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

    def sort(self) -> LinkedList[T]:
        pass

    def dedupe(self) -> LinkedList[T]:
        pass

    @staticmethod
    def merge(list1: LinkedList[T], list2: LinkedList[T]) -> LinkedList[T]:
        last = list1.get_last()
        last.next = list2
        return list1