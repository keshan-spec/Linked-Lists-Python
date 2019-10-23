class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
        current_node = self.head
        if not current_node:
            return

        new_node = Node(data)
        new_node.next = prev.next
        prev.next = new_node


cl = CLinkList()
cl.append('A')
cl.append('B')
cl.append('C')
cl.append('D')
cl.prepend('F')
# cl.append_after(cl.head.next, 'F')
cl.print_cllist()
