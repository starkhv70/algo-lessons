"""Linked list."""


class Node(object):
    """Represantation of member structure linked list."""

    def __init__(self, node_value):
        self.value = node_value  # noqa:WPS110
        self.next = None


class LinkedList(object):  # noqa:WPS214
    """Represantation of structure linked list."""

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_in_tail(self, item):  # noqa:WPS110
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, searching_value):
        node = self.head
        while node is not None:
            if node.value == searching_value:
                return node
            node = node.next
        return None

    def find_all(self, searching_value):
        found_nodes = []
        for node in self:
            if node.value == searching_value:
                found_nodes.append(node)
        return found_nodes

    def remove_node(self, previous_node, node):
        if self.head == self.tail:
            self.clean()
            return
        if node == self.tail:
            self.tail = previous_node
            self.tail.next = None
            return
        if node == self.head:
            self.head = self.head.next
        else:
            previous_node.next = node.next

    def delete(self, deleting_value, all=False):  # noqa:WPS125, WPS231, C901
        previous_node = None
        for node in self:
            if node.value == deleting_value:
                self.remove_node(previous_node, node)
                if not all:
                    return
            else:
                previous_node = node

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        return len(list(self))

    def insert(self, after_node, new_node):
        if (self.head is None) or (after_node == self.tail):
            self.add_in_tail(new_node)
            return
        if after_node is None:
            new_node.next = self.head
            self.head = new_node
            return
        new_node.next = after_node.next
        after_node.next = new_node
