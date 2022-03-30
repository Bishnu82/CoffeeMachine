from collections import deque

class Stack:

    def __init__(self):
        self._backing_deque = deque([])

    def push(self, el):
        self._backing_deque.append(el)

    def pop(self):
        return self._backing_deque.pop()

    def peek(self):
        return self._backing_deque[-1]

    def is_empty(self):
        return not bool(self._backing_deque)
