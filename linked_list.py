class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


l_list = LinkedList()
print(l_list)

first_node = Node("a")
l_list.head = first_node
print(l_list)

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(l_list)



