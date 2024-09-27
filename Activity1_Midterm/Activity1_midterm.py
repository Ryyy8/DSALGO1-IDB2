class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Stack after pushing {item}: {self.items}")

    def pop(self):
        if self.is_empty():
            return "Error: Stack is empty"
        item = self.items.pop()
        print(f"Popped item: {item}, Current stack: {self.items}")
        return item

    def top(self):
        if self.is_empty():
            return "Error: Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)



S = Stack()
operations = [
    ("S.push(5)",),
    ("S.push(3)",),
    ("len(S)",),
    ("S.pop()",),
    ("S.is_empty()",),
    ("S.pop()",),
    ("S.is_empty()",),
    ("S.pop()",),
    ("S.push(7)",),
    ("S.push(9)",),
    ("S.top()",),
    ("S.push(4)",),
    ("len(S)",),
    ("S.pop()",),
    ("S.push(6)",),
    ("S.push(8)",),
    ("S.pop()",)
]


for operation in operations:
    command = operation[0]
    if command.startswith("S.push"):
        value = int(command[7:-1])
        S.push(value)
    elif command == "len(S)":
        print(f"Current stack length: {len(S)}")
    elif command == "S.pop()":
        S.pop()
    elif command == "S.is_empty()":
        print(f"Is the stack empty? {S.is_empty()}")
    elif command == "S.top()":
        print(f"Top item: {S.top()}")

print()


stack = Stack()
operations2 = [
    ("push(5)",),
    ("push(3)",),
    ("pop()",),
    ("push(2)",),
    ("push(8)",),
    ("pop()",),
    ("pop()",),
    ("push(9)",),
    ("push(1)",),
    ("pop()",),
    ("push(7)",),
    ("push(6)",),
    ("pop()",),
    ("pop()",),
    ("push(4)",),
    ("pop()",),
    ("pop()",)
]


returned_values = []
for operation in operations2:
    command = operation[0]
    if command.startswith("push"):
        value = int(command[5:-1])
        stack.push(value)
    elif command == "pop()":
        returned_values.append(stack.pop())


print("\nReturned values from pop operations:", returned_values)
