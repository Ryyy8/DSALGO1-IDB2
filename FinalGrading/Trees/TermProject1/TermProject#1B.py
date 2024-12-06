class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer


class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


class DequeWithStackAndQueue:
    def __init__(self):
        self.stack = LinkedStack()
        self.queue = LinkedQueue()

    def is_empty(self):
        return self.stack.is_empty() and self.queue.is_empty()

    def __len__(self):
        return len(self.stack) + len(self.queue)

    def add_first(self, e):
        self.stack.push(e)

    def add_last(self, e):
        self.queue.enqueue(e)

    def remove_first(self):
        if self.stack.is_empty():
            raise Exception('Deque is empty')
        return self.stack.pop()

    def remove_last(self):
        if self.queue.is_empty():
            raise Exception('Deque is empty')
        return self.queue.dequeue()

    def first(self):
        if self.stack.is_empty():
            raise Exception('Deque is empty')
        return self.stack.top()

    def last(self):
        if self.queue.is_empty():
            raise Exception('Deque is empty')
        return self.queue.first()

    def print_deque(self):
        stack_elements = []
        while not self.stack.is_empty():
            stack_elements.append(self.stack.pop())
        queue_elements = []
        current = self.queue._head
        while current:
            queue_elements.append(current._element)
            current = current._next
        for element in reversed(stack_elements):
            self.stack.push(element)

        return stack_elements + queue_elements


try:
    print("Test started")
    deque = DequeWithStackAndQueue()

    deque.add_first(10)
    deque.add_last(20)
    deque.add_first(5)
    deque.add_last(30)
    deque.add_first(2)
    deque.add_last(40)
    deque.add_first(1)
    deque.add_last(50)

    print("First element:", deque.first())
    print("Last element:", deque.last())

    print("Deque list:", deque.print_deque())

    print("Removed first:", deque.remove_first())
    print("Removed last:", deque.remove_last())

    print("Length:", len(deque))

    print("Is empty?", deque.is_empty())
    print("Deque list:", deque.print_deque())
except Exception as e:
    print(f"Error: {e}")
