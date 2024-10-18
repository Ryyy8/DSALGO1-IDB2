class ArrayStack:
    '''LIFO Stack implementation using a Python List as a data structure.'''

    def __init__(self):
        '''Creating an empty stack.'''
        self.data = []

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return len(self.data)

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return len(self) == 0

    def push(self, val):
        '''Add new element to the top of the stack.'''
        self.data.append(val)

    def top(self):
        '''Return (but do not remove) the element at the top of the stack.'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data[-1]

    def pop(self):
        '''Remove and return the element at the top of the stack (i.e. LIFO).'''
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.pop()