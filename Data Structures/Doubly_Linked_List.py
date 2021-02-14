class Node():
    # the constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    
    # the initializer
    def __init__(self):
        # no data in the head
        self.head = None
        # make the tail point to the head
        self.tail = self.head
        # initialize length
        self.length = 0
        
    def print_list(self):
        if self.head == None:
            # if no data in the head
            print("Empty")
        else:
            # initialize a pointer to the node head
            current_node = self.head
            # continue as long as the pointer doesn't point to None
            while current_node != None:
                # print current node data
                print(current_node.data, end = ' ')
                # let the pointer move to the next data item in the LinkedList
                current_node = current_node.next
        # print a new line
        print()
    
    def append(self, data):
        # make a new node
        new_node = Node(data)
        if self.head == None:
            # if the linked list is empty, make the head and tail equal to the new node
            self.head = new_node
            self.tail = self.head
        else:
            # else let the new node previous pointer point to the current LinkedList tail
            new_node.previous = self.tail
            # let the LinkedList tail next pointer point to the new node
            self.tail.next = new_node
            # let the data in the LinkedList tail be the new node data thus updating the tail value
            self.tail = new_node
        # incrementing Linked List length by 1
        self.length += 1
        
    def prepend(self, data):
        new_node = Node(data)
        if self.data == None:
            # if the linked list is empty, make the head and tail equal to the new node
            self.head = new_node
            self.tail = self.head
        else:
            # else let the new node next pointer point to the current LinkedList head
            new_node.next = self.head
            # let the LinkedList head previous pointer point to the new node
            self.head.previous = new_node
            # let the data in the LinkedList head be the new node data thus updating the head value
            self.head = new_node
        # incrementing Linked List length by 1
        self.length += 1
        
    def insert(self, position, data):

        if position == 0:
            # inserting at the first position is the same as prepending
            self.prepend(data)
        elif position >= self.length:
            # inserting at the last position is the same as appending
            self.append(data)
        else:
            # creating a new node
            new_node = Node(data)
            # making a pointer to the Linked List head
            current_node = self.head
            # traversing until reaching the position just before the desired position
            for i in range(position - 1):
                current_node = current_node.next
            # making the previous of the new_node point to the curernt node
            new_node.previous = current_node
            # making the next of the new_node point to the next of the current node
            new_node.next = current_node.next
            # making the next of the current node point to the new_node
            current_node.next = new_node
            # making the previous of the next node point to the new_node instead of the
            # current_node
            new_node.next.previous = new_node
            # incrementing Linked List length by 1
            self.length += 1
