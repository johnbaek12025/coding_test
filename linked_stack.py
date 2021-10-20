class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, item):
        self.last = Node(item, self.last)
        return self.last     

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

def printNodes(node):    
    print(node.item, end = ' ')
    if node.next:
        printNodes(node.next)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)    
    printNodes(stack.push(5))
    # for _ in range(5):
    #     print(stack.pop())