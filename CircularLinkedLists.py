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
            nodes += f'[{current_node.data}]->'
            # print(f'Node->[{current_node.data}]', end='->')
            current_node = current_node.next
        print(nodes.strip('->'))

    def append(self, data):
        new_node = Node(data)
        current_node = self.head
        prev = None
        if current_node:
            while current_node:
                prev = current_node
                current_node = current_node.next
            prev.next = new_node
            return

        self.head = new_node

    def prepend(self, data):
        current_node = self.head
        if not current_node:
            return
        new_node = Node(data)
        self.head = new_node
        self.head.next = current_node
    # def prepend(self, prev, data):
    #     current_node = self.head
    #     if not current_node:
    #         return

    #     while current_node:
    #         if current_node.data == prev.data:
    #             prev = current_node
    #             current_node = current_node.next


cl = CLinkList()
cl.append('A')
cl.append('B')
cl.append('C')
cl.print_cllist()
