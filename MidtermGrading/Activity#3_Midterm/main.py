from ArrayStack import ArrayStack as Stack


def is_matched(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expr:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


def reverse_file(filename):
    stack = Stack()
    with open(filename, 'r') as file:
        for line in file:
            stack.push(line.strip())
    with open(filename, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')


if __name__ == "__main__":
    user_expr = input("Enter an expression to check for balanced symbols: ")
    if is_matched(user_expr):
        print("The symbols are balanced!")
    else:
        print("The symbols are not balanced.")

    filename = 'myfile.txt'
    reverse_file(filename)
    print(f"The contents of '{filename}' have been reversed.")
