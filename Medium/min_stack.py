"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []
         

    def push(self, val):
        if not self.stack:
            self.minimum.append(val)
        else:
            self.minimum.append(min(val, self.minimum[-1]))
        self.stack.append(val)


    def pop(self):
        self.stack = self.stack[:-1]
        self.minimum = self.minimum[:-1]
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minimum[-1]
