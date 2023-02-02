class Queue:

    def __init__(self):
        self.items = []
        self.len_queue = 0

    def is_empty(self):
        '''
        return true if queue is already full, else return false
        '''
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, item):
        '''
        insert data into queue
        '''
        if not self.is_max():
            self.items.append(item)
            self.len_queue += 1
        else:
            print("Queue is already full")

    def dequeue(self):
        '''
        remove first index in queue
        '''
        if self.is_empty():
            print("Cannot dequeue, queue is empty")
        else:
            self.len_queue -= 1
            return self.items.remove(self.items[0])

    def size(self):
        '''
        print length of queue
        '''
        print(self.len_queue)

    def is_max(self):
        '''
        return true if queue is full, else return false
        '''
        if self.len_queue == 10:
            return True
        else:
            return False

    def show_queue(self):
        '''
        print all data in queue
        '''
        print(self.items)


my_queue = Queue()

# dequeue
print(my_queue.is_empty())
print(my_queue.is_max())
my_queue.dequeue()
my_queue.show_queue()
my_queue.size()

# queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
my_queue.enqueue(7)
my_queue.enqueue(8)
my_queue.enqueue(9)
my_queue.enqueue(10)
my_queue.show_queue()

my_queue.enqueue(11)
my_queue.size()

# dequeue
my_queue.dequeue()
my_queue.size()
my_queue.show_queue()

# enqueue
my_queue.enqueue(11)
my_queue.show_queue()
print(my_queue.is_empty())
print(my_queue.is_max())


