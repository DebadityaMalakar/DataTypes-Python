class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
    def __init__(self):  
        self.head = None
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node
  
