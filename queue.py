from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()


    def enqueu(self,item):
        self.queue.append(item)


    def dequeu(self):

        if len(self.queue) > 0:

            return  self.queue.popleft()
        else:

            return None
        
    def __str__(self): 

        return str(self.queue)
    

#adding items in queue........ by enqueu
my_queue=Queue()    
my_queue.enqueu(3)
my_queue.enqueu(4)
my_queue.enqueu(8)
my_queue.enqueu(12)
print(my_queue)

#delete items in queue......... by dequeu
my_queue.dequeu()
my_queue.dequeu()
print(my_queue)