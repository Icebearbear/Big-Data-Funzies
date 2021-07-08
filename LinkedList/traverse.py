class node():
    def __init__(self) :
        self.data: None
        self.next: None
      
class LinkedList():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head == None:
            self.head = node() # set the head as a node
            self.head.data = data # set the head node's data
            self.head.next = None
        else:
            new_node = node()    
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next): # keep checking for the next of a node until it exist
                # print(temp.next.next)
                temp = temp.next # set the next next of that temp
            temp.next = new_node # set the next next of that node 
            
    def printList(self):
        temp = self.head
        while(temp):
            print('show ',temp.data)
            temp = temp.next
            
    def deleteList(self, key):
        if key == self.head :
            self.head = self.head.next
        else:
            temp = self.head
            while(temp): # iterate all nodes until the end and stop when theres no more nodes
                print('i ', temp.data)
                if temp.data == key:   # iteration keep going until temp data matches the key input
                    break               # when it matches it break the while loop and run line 44
                prev = temp # set previous temp to be current temp
                temp = temp.next # set current temp to be next temp to keep the iteration going
                print(prev.data, " ",temp.data," ", temp.next.data) 
                
        prev.next = temp.next   # delete the link between the matched key node with the next node
        # prev = 1
        # temp = matched node = 2
        # temp.next = 3
        # unlink temp to temp.next -->  prev.next = temp.next        
         
input = {1,2,3}
if __name__ == "__main__":
    n = LinkedList()
    
    for i in input:
        n.insert(i)
        
    # n.printList()
    
    n.deleteList(2)
    n.printList()
    
    
    