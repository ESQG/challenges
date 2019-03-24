"""Write a data structure that works like a stack (can push and pop in constant time)
and additionally has the following 3 functions: min, max, mean of all the numbers
currently on the stack.
Runtime = whatever you think you can do.
Or: min, max, mean, push, pop all constant time.

3 stacks
1. Main stack
2. Update/maintain min: add to the minstack
3. Update/maintain max: add to the maxstack
4. Number of items.
"""

from collections import deque

class MeanStack:

    def __init__(self):
        self._stack = deque()
        self._items = 0
        self._total = 0
        self._min_stack = deque()
        self._max_stack = deque()

    def push(self, value):
        self._stack.append(value)
        self._total += value

        if self._items == 0:
            self._min_stack.append(value)
            self._max_stack.append(value)
        else:
            min = self._min_stack[-1]
            if value <= min:
                self._min_stack.append(value)

            max = self._max_stack[-1]
            if value >= max:
                self._max_stack.append(value)

        self._items += 1

    def pop(self):
        if self._items <= 0:
            raise IndexError("MeanStack is empty")

        value = self._stack.pop()
        self._items -= 1
        self._total -= value

        min = self._min_stack[-1]
        if value == min:
            self._min_stack.pop()

        max = self._max_stack[-1]
        if value == max:
            self._max_stack.pop()

        return value

    def get_max(self):
        if self._items <= 0:
            raise IndexError("MeanStack is empty")

        return self._max_stack[-1]

    def get_min(self):
        if self._items <= 0:
            raise IndexError("MeanStack is empty")

        return self._min_stack[-1]

    def get_mean(self):
        if self._items == 0:
            return 0

        return self._total / self._items
