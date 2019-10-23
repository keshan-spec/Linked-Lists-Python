class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
        if current_node:
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = new_node
            new_node.next = self.head
            return

        self.head = new_node
        self.head.next = self.head

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


# cl.prepend('F')
# cl.remove('B')
# cl.append_after(cl.head.next, 'K')
cl.print_cllist()
