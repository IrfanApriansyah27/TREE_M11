"""
Irfan Apriansyah
2IA26
50422717
"""

class TreeNode:
    def __init__(self, key):
        # Konstruktor untuk membuat simpul (node) dalam pohon
        self.key = key
        self.left = None
        self.right = None


def sorted_list_to_bst(sorted_list):
    # Fungsi untuk mengonversi daftar yang sudah diurutkan menjadi pohon biner yang seimbang
    if not sorted_list:
        return None

    mid = len(sorted_list) // 2
    root = TreeNode(sorted_list[mid])

    root.left = sorted_list_to_bst(sorted_list[:mid])
    root.right = sorted_list_to_bst(sorted_list[mid + 1:])

    return root


def print_tree(root, level=0, prefix="Root: "):
    # Fungsi untuk mencetak struktur pohon secara rekursif
    if root:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")


# Contoh penggunaan
sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
balanced_tree_root = sorted_list_to_bst(sorted_list)
print_tree(balanced_tree_root)
