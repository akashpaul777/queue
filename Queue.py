class Node(object):
    '''
    Singly-linked list node for storing data in
    a queue
    '''
    def __init__(self, data=None):
        '''
        Initialise a Node with optional data to be stored
        '''
        self.right = None
        self.data = data
    
class Queue(object):
    '''
    Queue structure implemented using a singly-linked list
    '''
    def __init__(self):
        '''
        Initialise an empty queue
        '''
        self.first = None
        self.last = None

    def enqueue(self, data):
        '''
        Enqueue data; putting it on the back of the queue
        '''
        new_node = Node(data)
        if self.first is None and self.last is None:
            # case 1: no nodes exist
            self.first = new_node
            self.last = self.first
        else:
            # case 2: at least one node exists
            self.last.right = new_node
            self.last = new_node
    
    def dequeue(self):
        '''
        Dequeue data; removing it from the front of the queue
        '''
        if self.first is None:
            # case 1: nothing on the queue
            return None
        else:
            # case 2: something on the queue
            data = self.first.data
            next = self.first.right
            if next is None:
                # case 1: nothing else queued
                self.first = None
                self.last = None
            else:
                # case 2: something else queued
                self.first = next
            return data

if __name__ == '__main__':
    # Test the queue
    q = Queue()
    print q.dequeue()
    q.enqueue(1)
    print q.dequeue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print q.dequeue()
    q.enqueue('d')
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()