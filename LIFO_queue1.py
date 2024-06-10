import queue

my_queue = queue.LifoQueue(maxsize=4)

 

my_queue.put(9)
my_queue.put(99)
my_queue.put(999)
my_queue.put(9999)

print("check queue size")
print("Queue Size:", my_queue.qsize())


print("======================")
print("check queue is empty or not(After put elements)")
print("Empty:", my_queue.empty())


print("======================")
print("check queue is full or not(After put elements)")
print("Full:",my_queue.full())


print("\n===Remove elements===\n")
print(my_queue.get())
print(my_queue.get())
print(my_queue.get())
print(my_queue.get())


print("======================")
print("check queue is full or not(After remove elements)")
print("Full:",my_queue.full())


print("======================")
print("check queue is empty or not(After remove elements)")
print("Empty:", my_queue.empty())



