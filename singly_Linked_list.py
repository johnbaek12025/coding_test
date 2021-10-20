class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def iterative_printNodes(node: ListNode):
    # iterative method
    crnt_node = node
    while crnt_node:
        print(crnt_node.val, end=' ')
        crnt_node = crnt_node.next

def recursive_printNodes(node: ListNode):
    # recursive method there must be a constraint about a boarder line    
    print(node.val, end = ' ')
    if node.next:
        recursive_printNodes(node.next)

class SLinkedList:
    def __init__(self): 
        self.head = None

    def addAtHead(self, val):
        # 새로 넣은 val을 head로 하고, 이전의 node는 head.next로  
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addBack(self, val):
        """
        1. 받은 val에 대해 node 생성
        2. addAtHead에서 생성한 head를 crnt_node로 지정
        3. crnt_node의 next가 있는 동안
        4. 가장 마지막 node까지 이동
        5. 가장 마지막 node.next에 생성된 새로운 node 할당
        ※ linked_list에 아무것도 없을 떄는 이 함수가 동작 하지 않음
        """
        node = ListNode(val) 
        crnt_node = self.head  
        while crnt_node.next:
            crnt_node = crnt_node.next
        crnt_node.next = node

    def findNode(self, val):
        """
        find_node는 입력 받은 argument에 대해
        찾는 method로 
        crnt_node를 self.head로 받고,
        crnt_node.next가 존재하는 동안
        crnt_node.val을 argument val와 비교하면서
        같으면 현재 crnt_node를 return
        값이 존재 하지 않으면 raise 함수를 사용하여
        runtime error 발생시킨다.

        find_node는 node insertion or node deletion을 위해 구성
        """
        crnt_node =  self.head
        while crnt_node:
            if crnt_node.val == val:
                return crnt_node
            crnt_node = crnt_node.next
        raise RuntimeError('Node not found')

    def addAfter(self, node, val):
        """
        arguments로 node와 val을 받고,
        val에 대해 새로운 node를 만든다.
        new_node.next에 node.next를 할당하고,
        node.next에 new_node를 할당
        """
        new_node = ListNode(val)
        new_node.next = node.next
        node.next = new_node
    
    def deleteAfter(self, prev_node):
        """
        삭제하고자 하는 node의 이전 node를 argument로 받는다.
        해당 prev_node.next가 존재하면 prev_node.next를 
        prev_node.next.next로 할당
        """
        if prev_node.next:
            prev_node.next = prev_node.next.next

    def recursive(self, node: ListNode) -> ListNode:
        # 삭제해야할 node가 head인 경우
        if not node:
            return None
        next_node = self.recursive(node.next)
        if node.val == self.__val: # 현재 node의 값이 삭제하고자 하는 val과 같으면
            return next_node
        else:
            node.next = next_node
            return node


if __name__ == '__main__':
    slist = SLinkedList()
    slist.addAtHead(1)
    slist.addAtHead(2)
    slist.addBack(3)

    node1 = slist.findNode(2)
    slist.addAfter(node1, 4)    
    slist.deleteAfter(node1)
    recursive_printNodes(slist.head)
