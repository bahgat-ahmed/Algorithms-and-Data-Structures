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
        # make a new node
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
            
    def delete_by_value(self, data):
        if self.head == None:
            # if Linked List is empty
            print("Linked List is empty. There is nothing to delete.")
            # get out of the function
            return
        if (self.length == 1) or (self.length == 2):
            # if Linked List contains one or two nodes
            if (self.head.data != data) and (self.tail.data != data):
                # if value isn't found
                print('Value not found!')
            elif self.length == 1:
                # if value is found and there is only one Node, then point head to Null
                self.head = None
                # point tail to head
                self.tail = self.head
            elif self.head.data == data:
                # if value is found at the Linked List head, and there are two nodes, point head to tail
                self.head = self.tail
            elif self.tail.data == data:
                # if value is found at the Linked List tail, and there are two nodes, point tail to head
                self.tail = self.head
            # decrementing Linked List length by 1
            self.length -= 1
                
        else:
            # if Linked List contains more than one node
            # position tracker
            current_pos = 0
            # make a pointer to the Linked List head
            current_node = self.head
            # traverse through the list until you find the data, and change the position accordingly
            while (current_node.data != data) and (current_pos <= self.length - 1):
                current_node = current_node.next
                current_pos += 1
                
            if current_node.data != data:
                # if value isn't found
                print('Value not found!')
            else:
                # if the value is found at the Linked List head
                if current_pos == 0:
                    # make the head point to the next node
                    self.head = current_node.next
                    # point the current_node next, and previous pointers to Null
                    current_node.previous = None
                    current_node.next = None
                # if value is found at the Linked List tail
                elif current_pos == self.length - 1:
                    # point the previous node next pointer to Null
                    current_node.previous.next = None
                    # point the current node previous pointer to Null
                    current_node.previous = None
                # if value is found at some where in the middle of the Linked List
                else:
                    # point the previous node next pointer to the next node 
                    current_node.previous.next = current_node.next
                    # point the next node previous pointer to the previous node
                    current_node.next.previous = current_node.previous
                    # point the current_node previous, and next pointers to Null
                    current_node.previous = None
                    current_node.next = None
                    
                # decrementing Linked List length by 1
                self.length -= 1
                
    def delete_by_position(self, position):
        # handling invalid inputs
        # given that the input position is zero index-based (i.e. first position starts from zero)
        if self.head == None:
            # if Linked List is empty
            print("Linked List is empty. There is nothing to delete.")
            # get out of the function
            return
        if (position < 0) and (position > self.length - 1):
            print("This position doesn't exist in the Linked List!")
            # get out of the function
            return
        # handling valid inputs
        # if the first position is chosen
        if position == 0:
            # update the Linked List head to be the next node
            self.head = self.head.next
            # if the Linked List had only one or two nodes before deleting the first node
            if (self.head == None) or (self.head.next == None):
                # make the tail point to the head
                self.tail = self.head
            # else if the Linked List had more than two nodes before deleting the first node
            elif self.head != None:
                # make the previous pointer of the new head point to Null
                self.head.previous = None
        # if the last position is chosen
        elif position == self.length - 1:
            # make the next pointer of the node before the last node point to Null
            self.tail.previous.next = None
            # make the previous pointer of the last node point to Null to delete this node
            self.tail.previous = None
        # if a position somewhere in the middle is chosen
        else:
            # track the Linkded List for traversing, starting form its head
            current_node = self.head
            # traverse throught the Linked List until you find the position you want to delete
            for i in range(position - 1):
                current_node = current_node.next
            # make the next pointer of the previous node point to the next node
            current_node.previous.next = current_node.next
            # make the previous pointer of the next node point to the previous node
            current_node.next.previous = current_node.previous
            # make the previous pointer of the current node point to Null for deleting its first link
            current_node.previous = None
            # make the next pointer of the current node point to Null for deleting it completely from the
            # Linked List
            current_node.next = None
        # decrementing Linked List length by 1  
        self.length -= 1
