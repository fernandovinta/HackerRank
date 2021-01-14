def check_binary_search_tree_(root):
    return (isBts(root, 0, (10 ** 4)))

def isBts(node, min, max):
    if node is None:
        return True
    if node.data < min or node.data > max: 
        return False
    return (isBts(node.left, min, node.data - 1)) and (isBts(node.right, node.data + 1, max))
