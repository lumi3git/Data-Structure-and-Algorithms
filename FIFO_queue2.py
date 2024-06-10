import queue

my_queue2 = queue.Queue(maxsize=6) 

my_queue2.put(2)
my_queue2.put(22)
my_queue2.put(222)
my_queue2.put(2222)
my_queue2.put(22222)


print("Queue Size:",my_queue2.qsize(),"\n")


print("After put elements")
print("======================")
print("Empty:", my_queue2.empty())


print("Full:", my_queue2.full(),"\n")


print(my_queue2.get())
print(my_queue2.get())
print(my_queue2.get(),"\n")


print("After remove elements")
print("======================")
print("Full:", my_queue2.full())


print("empty:", my_queue2.empty())
