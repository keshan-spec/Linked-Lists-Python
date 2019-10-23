from Node import Node

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

    def merge_sorted(self, llist):
        merged_list = None
        list_1 = self.head
        list_2 = llist.head

        if not list_1:
            return list_2
        if not list_2:
            return list_1

        if list_1 and list_2:
            if list_1.data <= list_2.data:
                merged_list = list_1
                list_1 = merged_list.next

            else:
                merged_list = list_2
                list_2 = merged_list.next
            new_head = merged_list

        while list_1 and list_2:
            if list_2.data <= list_1.data:
                merged_list.next = list_2
                merged_list = list_2
                list_2 = merged_list.next
            else:
                merged_list.next = list_1
                merged_list = list_1
                list_1 = merged_list.next

        if not list_1:
            merged_list.next = list_2
        if not list_2:
            merged_list.next = list_1

        return new_head

        # print(list_1.data, list_2.data)

    def remove_duplicates(self):
        current_node = self.head
        prev = None
        unique = {}
        while current_node:
            if current_node.data in unique:
                prev.next = current_node.next
                current_node = None
            else:
                unique[current_node.data] = 1
                prev = current_node
            current_node = prev.next

    def occurances(self, data):
            # Iterative
        count = 0
        pointer = self.head

        while pointer:
            if pointer.data == data:
                count += 1
            pointer = pointer.next

        print(f'{data} has {count} occurances')
        return count

    def occurances_recursive(self, node, data):
        # Recursive
        if not node:
            return 0
        if node.data == data:
            node = node.next
            return 1 + self.occurances_recursive(node, data)
        else:
            return self.occurances_recursive(node.next, data)

    def nth_from_last(self, n):
        # Method one
        # length = self.len_iter()
        # current_node = self.head
        # while current_node:
        #     if length == n:
        #         print(current_node.data)
        #         return current_node
        #     length -= 1
        #     current_node = current_node.next
        # if current_node == None:
        #     return

        # Method two
        pointer = self.head
        q = self.head
        count = 0
        while q and count < n:
            q = q.next
            count += 1
        if not q:
            print("Invalid length in Linked List")
            return
        while pointer and q:
            pointer = pointer.next
            q = q.next

        print(pointer.data)

    def rotate(self, k):
        prev = None
        pointer = self.head
        q = self.head
        count = 1

        while pointer and count <= k:
            prev = pointer
            pointer = pointer.next
            count += 1
        pointer = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = pointer.next
        pointer.next = None

    def is_palindrome(self):
        current_node = self.head
        palindrome = []
        while current_node:
            palindrome.append(current_node.data)
            current_node = current_node.next

        return palindrome[::-1] == palindrome[:]


# Linke List object
llist = LinkedList()
llist.append('R')
llist.append('A')
llist.append('C')
llist.append('E')
llist.append('C')
llist.append('A')
llist.append('R')

# llist.occurances(5)
# llist.occurances_recursive(llist.head, 5)
# llist.remove_duplicates()
# llist.prepend(6)
# llist.insert_after_node(llist.head, 5)
# llist.delete_node('C')
# llist.delete_node_at(1)
# llist.len_iter()
# llist.len_recursive(llist.head)
# llist.merge_sorted
# print(llist.is_palindrome())
llist.print_list()
