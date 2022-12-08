
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    root = BinarySearchTreeNode(elements)
    return root
            
if __name__ == '__main__':
    status=[]
    count=0
    while (True):    
        count += 1    
        com_data = input()
        if com_data=='0':
            break
        com_data = com_data.split()
        com = int(com_data[0])
        data = int(com_data[1])
        if com==1 and count==1:
            status_tree = build_tree(data)
        # elif com==2 and count==1:
        #     status.append(0) 
        # elif com==3 and count==1:
        #     continue
        else:
            if com==1:
                status_tree.add_child(data)
            elif com==2:
                if (status_tree.search(data)==True):
                    status.append(1)
                else:
                    status.append(0)
            elif com==3:
                status_tree.delete(data)
    for i in status:
        print(i)