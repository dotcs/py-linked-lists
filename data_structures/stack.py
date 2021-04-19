from .linked_list import LinkedList, T
from typing import Generic, Optional


class Stack(Generic[T]):
    _linked_list: Optional[LinkedList[T]] = None
    _size: int = 0
    _top: Optional[LinkedList[T]] = None

    def is_empty(self) -> bool:
        return self.size() == 0

    def size(self) -> int:
        return self._size

    def top(self) -> Optional[T]:
        if self.is_empty():
            return None
        assert self._top is not None
        return self._top.data

    def push(self, data: T) -> None:
        if self.is_empty():
            node = LinkedList(data)
            self._linked_list = node
        else:
            assert self._linked_list is not None
            node = LinkedList(data)
            self._linked_list.next = node
        self._top = node
        self._size += 1

    def pop(self) -> Optional[T]:
        if self.is_empty():
            return None

        cur = self._linked_list
        assert self._top is not None
        node = self._top
        for _ in range(self.size() - 2):
            assert cur is not None
            cur = cur.next
        self._top = cur
        assert self._top is not None
        self._top.next = None
        self._size -= 1

        return node.data
