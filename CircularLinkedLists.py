from Node import Node
from SingleLinkedList import LinkedList

"""
<Circular linked List class>
Example :
            1->2->3->1
This linked list does not have a null ending pointer. the node before last is
next to the head node
Here 1 is the head node and 3 is the node before last and it is curularly next to the head

"""


class CLinkList:
    def __init__(self):
        self.head = None

    def print_cllist(self):
        current_node = self.head
        nodes = ''
        while current_node:
            nodes += f'[{current_node.data}]->[{current_node.next.data}]\n'
            # print(f'Node->[{current_node.data}]', end='->')
            current_node = current_node.next
            if current_node == self.head:
                break
        print(nodes)

    def append(self, data):
        """
        Params:
            data -> the data for the new node
        Usage: Adds the new node to the start of the linked list as the new head
        or appends the node to the existing chain of nodes
        """
        new_node = Node(data)
        current_node = self.head
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        """
        Params:
            data -> the data for the new node
        Usage: Adds the new node to the start of the linked list as the new head
        """
        current_node = self.head
        new_node = Node(data)

        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            self.head = new_node

    def append_after(self, prev, data):
        """
        Params:
            Prev -> Previous node or the that you want to append the new node next to
            Data -> the data for the new node
        Usage: Appends a new node inbetween the given previous node
        """
        current_node = self.head
        if not current_node:
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node

    def remove(self, key):
        """
        Params :
            Key -> the data of the node that needs to be removed
            Usage: Removes a specific node and updates  the nodes
        """
        current_node = self.head
        if self.head.data == key:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            while current_node:
                prev = current_node
                current_node = current_node.next
                if current_node.data == key:
                    break

            prev.next = current_node.next
            current_node = None

    def remove_node(self, node):
        current_node = self.head
        if self.head == node:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
        else:
            prev = None
            while current_node:
                prev = current_node
                current_node = current_node.next
                if current_node == node:
                    break

            prev.next = current_node.next
            current_node = None

    def __len__(self):
        count = 0
        node = self.head

        while node:
            count += 1
            node = node.next
            if node == self.head:
                break
        return count

    def split(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head.data

        mid = size // 2
        count = 0
        current_node = self.head
        prev = None
        while current_node and count < mid:
            count += 1
            prev = current_node
            current_node = current_node.next
        prev.next = self.head
        split_clist = CLinkList()
        while current_node.next != self.head:
            split_clist.append(current_node.data)
            current_node = current_node.next
        split_clist.append(current_node.data)
        return self, split_clist

    def josephus_circ(self, step):
        current_node = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                current_node = current_node.next
                count += 1
            print(f'Removed -> {current_node.data}')
            self.remove_node(current_node)
            current_node = current_node.next

    def is_circular_ll(self, inp_list):

        # Circular Linked list class object
cl = CLinkList()
"""
Example:
    Node A is the head
    Node D is the tail
    [A] -> [B]
    [B] -> [C]
    [C] -> [D]
    [D] -> [A]
"""
cl.append('A')
cl.append('B')
cl.append('C')
cl.append('D')
cl.append('E')
cl.append('F')
# cl.remove_node(cl.head.next)
cl.josephus_circ(2)

# split_1, split_2 = cl.split()
# split_1.print_cllist()
# split_2.print_cllist()
# cl.prepend('F')
# cl.remove('B')
# cl.append_after(cl.head.next, 'K')
cl.print_cllist()
