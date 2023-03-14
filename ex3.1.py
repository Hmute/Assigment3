import sys
from collections import deque

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
    
    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        return value
    
    def is_empty(self):
        return self.head is None

def evaluate_expression(expression):
    stack = Stack()
    num_parens = 0
    for token in expression.split()[::-1]:
        if token.isdigit():
            stack.push(int(token))
        elif token in ["+", "-", "*", "/"]:
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.push(a + b)
            elif token == "-":
                stack.push(a - b)
            elif token == "*":
                stack.push(a * b)
            elif token == "/":
                stack.push(a // b)
        elif token == ")":
            num_parens += 1
        elif token == "(":
            num_parens -= 1
            if num_parens < 0:
                raise ValueError("Mismatched parentheses")
        else:
            raise ValueError("Invalid token: " + token)
    if num_parens != 0:
        raise ValueError("Mismatched parentheses")
    if stack.is_empty():
        raise ValueError("Empty expression")
    return stack.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex3.1.py <expression>")
        sys.exit(1)
    expression = sys.argv[1]
    result = evaluate_expression(expression)
    print(result)