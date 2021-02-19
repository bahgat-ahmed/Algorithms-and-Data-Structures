class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BST():
    def __init__(self):
        self.root = None
        self.num_of_nodes = 0
        
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node    
        else:
            current_node = self.root
            while (current_node.right != new_node) and (current_node.left != new_node):
                try:
                    if (data > current_node.data):
                        if current_node.right != None:
                            current_node = current_node.right
                        else:
                            current_node.right = new_node

                    elif (data < current_node.data):
                        if current_node.left != None:
                            current_node = current_node.left
                        else:
                            current_node.left = new_node
                    else:
                        raise ValueError("This value already exists in the Binary Search Tree.")
                except ValueError:
                    raise
                    
        self.num_of_nodes += 1
        
    def search(self, data):
        if self.root == None:
            print("The Tree is Empty.")
        else:
            current_node = self.root
            for i in range(self.num_of_nodes):
                if data == current_node.data:
                    print("Value is found")
                    return
                elif data > current_node.data:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
            print("Value is not found")
