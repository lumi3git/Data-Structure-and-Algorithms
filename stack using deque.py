from collections import deque

stack=deque() #create an empty deque

stack.append(11) #puh elements to the stack
stack.append(22)
stack.append(33)
stack.append(44)
stack.append(55)

print(stack) #deque([11, 22, 33, 44, 55])

x = stack.pop() #pop() an element from the stack
print(x) #55,Because STACK follows LIFO

y = stack.pop()
print(y) #44

z = stack.pop()
print(z) #33

print(stack) #deque([11, 22])
