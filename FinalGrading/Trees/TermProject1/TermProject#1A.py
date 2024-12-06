from LinkedStack import LinkedStack

class DequeWithTwoStacks:

    def __init__(self):
        self.stack1 = LinkedStack()
        self.stack2 = LinkedStack()

    def is_empty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def add_first(self, e):
        self.stack1.push(e)

    def add_last(self, e):
        self.stack2.push(e)

    def remove_first(self):
        if self.stack1.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        if self.stack1.is_empty():
            raise Exception("Deque is empty!")
        return self.stack1.pop()

    def remove_last(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise Exception("Deque is empty!")
        return self.stack2.pop()

    def first(self):
        if self.stack1.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        if self.stack1.is_empty():
            raise Exception("Deque is empty!")
        return self.stack1.top()

    def last(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise Exception("Deque is empty!")
        return self.stack2.top()

    def print_deque(self):
        # Gather elements from stack1 and stack2
        stack1_elements = []
        while not self.stack1.is_empty():
            stack1_elements.append(self.stack1.pop())
        stack2_elements = []
        while not self.stack2.is_empty():
            stack2_elements.append(self.stack2.pop())

        # Refill stacks with elements
        for element in reversed(stack2_elements):
            self.stack2.push(element)
        for element in reversed(stack1_elements):
            self.stack1.push(element)

        # The final deque is stack1 elements followed by stack2 elements
        return stack1_elements + stack2_elements

try:
    deque = DequeWithTwoStacks()
    deque.add_first(10)
    deque.add_last(20)
    deque.add_first(5)
    deque.add_last(30)

    print("First element:", deque.first())
    print("Last element:", deque.last())

    print("Removed first:", deque.remove_first())
    print("Removed last:", deque.remove_last())

    print("Length:", len(deque))

    print("Is empty?", deque.is_empty())

    print("Deque list:", deque.print_deque())

except Exception as e:
    print(f"Error: {e}")
