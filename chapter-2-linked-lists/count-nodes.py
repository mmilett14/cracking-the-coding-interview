# Problem from https://www.youtube.com/watch?v=WwfhLC16bis

class Node:
  
  def __init__(self, data):
    self.data = data
    self.next = None
    
class LinkedList:
  
  def __init__(self):
    self.head = None
    
llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second

second.next = third

third.next = fourth

def countNodes(head):

    node_counter = 1
    next_node = head.next

    while next_node != None:
        node_counter +=1
        next_node = next_node.next
        
    return node_counter
