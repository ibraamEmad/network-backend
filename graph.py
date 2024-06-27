from typing import List, Dict, Tuple

class Node:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.children: List['Node'] = []

    def add_child(self, child_node: 'Node'):
        self.children.append(child_node)

    def to_nodes_and_edges(self) -> Tuple[List[Dict], List[Dict]]:
        nodes = []
        edges = []

        def traverse(node: 'Node'):
            nodes.append({
                "id": node.id,
                "label": node.name,
                "title": f"{node.name} tooltip text"
            })
            for child in node.children:
                edges.append({
                    "from": node.id,
                    "to": child.id
                })
                traverse(child)

        traverse(self)
        return nodes, edges

# Create the tree nodes with unique IDs
node1 = Node(1, 'Node 1')
node2 = Node(2, 'Node 2')
node3 = Node(3, 'Node 3')
node4 = Node(4, 'Node 4')
node5 = Node(5, 'Node 5')
node6 = Node(6, 'Node 6')
node7 = Node(7, 'Node 7')
node8 = Node(8, 'Node 8')

# Build the tree structure
node1.add_child(node2)
node1.add_child(node3)
node2.add_child(node4)
node2.add_child(node5)
node3.add_child(node6)
node3.add_child(node7)
node3.add_child(node8)