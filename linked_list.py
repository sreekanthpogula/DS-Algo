class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Traversing
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Inserting at begining
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Inserting at the End
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # Inserting between two nodes - before and after  existing node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Removing a node
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Reversing a LinkedList
    def reverse_linked_list(self):
        head = self.head
        if head is None or head.next is None:
            return head

        rest = self._reverse_linked_list(head.next)

        head.next.next = head
        head.next = None

        self.head = rest
        return self

    def _reverse_linked_list(self, head):
        if head is None or head.next is None:
            return head

        rest = self._reverse_linked_list(head.next)

        head.next.next = head
        head.next = None

        return rest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


l_list = LinkedList()
print("Linkedlist", l_list)

first_node = Node("a")
l_list.head = first_node
print("Linkedlist with head", l_list)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print("Linkedlist with updated node values", l_list)

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

llist = LinkedList()
print(llist)

llist.add_first(Node("b"))
print(llist)
llist.add_first(Node("a"))
print(llist)

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

llist.add_last(Node("f"))
print(llist)

llist.add_after("a", Node("b"))
llist = LinkedList(["a", "b", "c", "d"])

llist.add_after("c", Node("cc"))

llist.add_before("b", Node("aa"))
print(llist)
llist.add_before("c", Node("bb"))
print(llist)

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)
llist.remove_node("a")
print(llist)

head = LinkedList(["1", "2", "3", "4", "5"])
print(head)

new_head = LinkedList.reverse_linked_list(head)
print(new_head)

llist = LinkedList(["a", "b", "c", "d", "e"])
# print(LinkedList.__iter__(llist))

for node in llist:
    print(node)





