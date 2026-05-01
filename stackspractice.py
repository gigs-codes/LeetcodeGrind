# stack=[]

# push
# stack.append('A')
# stack.append('B')
# stack.append('C')
# stack.append('D')
# print("Stack is : ", stack)

# peek method
# topElement = stack[-1]
# print("peek: ", topElement)

# pop method

# popelement = stack.pop(-1)
# print(stack)
# print("pop : ",stack[-1])

# isEmpty method
# isEmpty = not bool(stack)
# print("isEmpty : ", isEmpty)

# size
# print("Size is : ", len(stack))

# stack class
class Stack:
    def __init__(self) -> None:
        # Its job is to initialize (set up) the object’s data
        self.stack = []

        def push(self,element):
            self.stack.append(element)

        def pop(self, element):
            if self.isEmpty():
                return "Stack is empty"
            return self.stack.pop()
        
        def peek(self):
            if self.isEmpty():
                return "Stack is empty"
            return self.stack(-1)
        
        def isEmpty(self):
            return len(self.stack) == 0
        
        def size(Self):
            return len(self.stack)

    myStack=Stack()

    myStack.push('A')
    myStack.push('B')
    myStack.push('C')
    myStack.push('D')

    print("Stack : ", myStack.stack)
    print("Pop : ",myStack.pop())
    print("Stack after pop : ",myStack.stack()) 