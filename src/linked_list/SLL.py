from node import Node


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def insert(self, value, location: int):
        node = Node(value=value, next_=None)

        if location == 1:
            node.next = self.head
            self.head = node
            self.tail = node

        elif location == self.num_nodes + 1:
            self.tail.next = node
            self.tail = node

        else:
            current_node = self.head
            for i in range(location - 2):
                current_node = current_node.next
            node.next = current_node.next
            current_node.next = node

        self.num_nodes += 1

    def print_linked_list(self):
        current = self.head
        nodes = []
        while current.next is not None:
            nodes.append(current)
            current = current.next
        nodes.append(current)
        print(" -> ".join([i.value for i in nodes]))
