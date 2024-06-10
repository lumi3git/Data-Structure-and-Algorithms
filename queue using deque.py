#importing deque
from collections import deque

#Creating a deque object
queue = deque()

queue.append(10) #enqueue,adds the element 10 to the right end of the deque
queue.append(20)
queue.append(30)

print(queue) #deque([10, 20, 30])

x=queue.popleft() #dequeue, QUEUE follows FIFO 
print(x) #10

x=queue.popleft() 
print(x) #20

print(queue) #deque([30])

