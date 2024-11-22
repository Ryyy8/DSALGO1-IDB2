def prec(c):
    if c == '^':
        return 3
    elif c in ('/', '*'):
        return 2
    elif c in ('+', '-'):
        return 1
    else:
        return -1

def infixToPostfix(expression):
    stack = []
    result = ""

    for char in expression:
        if char.isalnum():
            result += char + " "
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result += stack.pop() + " "
            if stack:
                stack.pop()
        else:
            while stack and prec(char) <= prec(stack[-1]):
                result += stack.pop() + " "
            stack.append(char)

    while stack:
        result += stack.pop() + " "

    return result.strip()

exp = input("Enter an infix expression: ")
postfix_result = infixToPostfix(exp)
print("Postfix expression:", postfix_result)

def insertion_sort_ascending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

numbers_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, numbers_input.split()))

ascending_numbers = numbers.copy()
insertion_sort_ascending(ascending_numbers)
print("Sorted in ascending order:", ascending_numbers)

descending_numbers = numbers.copy()
insertion_sort_descending(descending_numbers)
print("Sorted in descending order:", descending_numbers)

