class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        nodes = ''
        while current_node:
            nodes += f'[{current_node.data}]->'
            # print(f'Node->[{current_node.data}]', end='->')
            current_node = current_node.next
        print(nodes.strip('->'))

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


# Linke List object
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.print_list()
