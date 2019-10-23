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

    def helper(self, node, name):
        if node is None:
            print(f'{name} : None')
        else:
            print(f'{name} : {node.data}')

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("[-] Prev node is not valid")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next

        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            return

    def delete_node_at(self, index):
        current_node = self.head
        if current_node and index == 0:
            self.head = current_node.next
            current_node = None
            return

        prev = None
        count = 0
        while current_node and count != index:
            prev = current_node
            current_node = current_node.next
            count += 1

        if current_node:
            prev.next = current_node.next
            current_node = None
            return
        else:
            return

    def len_iter(self):
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def len_recursive(self, node):
        if node == None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key1, key2):
        current_node = self.head
        current_node_2 = self.head
        prev_1 = None
        prev_2 = None
        if key1 == key2:
            return

        while current_node and current_node.data != key1:
            prev_1 = current_node
            current_node = current_node.next

        while current_node_2 and current_node_2.data != key2:
            prev_2 = current_node_2
            current_node_2 = current_node_2.next

        if not current_node or not current_node_2:
            return

        if prev_1:
            prev_1.next = current_node_2
        else:
            self.head = current_node_2
        if prev_2:
            prev_2.next = current_node
        else:
            self.head = current_node
        current_node.next, current_node_2.next = current_node_2.next, current_node.next

    def reverse_iter(self):
        current_node = self.head
        prev = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev
            self.helper(prev, "PREV")
            self.helper(current_node, "CURRENT")
            self.helper(next_node, "NEXT")
            print('')
            prev = current_node
            current_node = next_node
        self.head = prev

    def reverse_recursive(self):
        def _recursive(current_node, prev_node):
            if not current_node:
                return prev_node

            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            return _recursive(current_node, prev_node)
        self.head = _recursive(self.head, None)


# Linke List object
llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
# llist.prepend(6)
# llist.insert_after_node(llist.head, 5)
# llist.delete_node('C')
# llist.delete_node_at(1)
# llist.len_iter()
# llist.len_recursive(llist.head)
llist.print_list()
