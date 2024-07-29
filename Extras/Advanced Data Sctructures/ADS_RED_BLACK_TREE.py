class node_block:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.parent = None
        self.red = False
        self.val = value
        
        
class Tree:
    def __init__(self):
        self.sentinel = node_block(0)
        self.sentinel.red = False
        self.root = self.sentinel
        
    def repair_RB_Tree(self,nd):
        while nd is not self.root and nd.parent.red is True:
            if nd.parent is nd.parent.parent.right:
                tmp = nd.parent.parent.left #sibling of curent nodes parent
                if tmp.red is True:
                    tmp.red = False
                    nd.parent.red = False
                    nd.parent.parent.red = True
                    nd = nd.parent.parent
                else:
                    if nd is nd.parent.left:
                        nd = nd.parent
                        self.right_rotation(nd)
                    nd.parent.red = False
                    nd.parent.parent.red = True
                    self.left_rotation(nd.parent.parent)
            else:
                tmp = nd.parent.parent.right
                if tmp.red is True:
                    tmp.red = False
                    nd.parent.red = False
                    nd.parent.parent.red = True
                    nd = nd.parent.parent
                else:
                    if nd is nd.parent.right:
                        nd = nd.parent
                        self.left_rotation(nd)
                    nd.parent.red = False
                    nd.parent.parent.red = True
                    self.right_rotation(nd.parent.parent)
                
        self.root.red = False
        
        
    def left_rotation(self,nd):
    
        tmp = nd.right
        nd.right = tmp.left
        if tmp.left is not self.sentinel:
            tmp.left.parent = nd

        tmp.parent = nd.parent
        if nd.parent is None:
            self.root = tmp
        elif nd is nd.parent.left:
            nd.parent.left = tmp
        else:
            nd.parent.right = nd
        tmp.left = nd
        nd.parent = tmp

    def right_rotation(self,nd):
        tmp = nd.left
        nd.left = tmp.right
        if tmp.right is not self.sentinel:
            tmp.right.parent = nd

        tmp.parent = nd.parent
        if nd.parent is None:
            self.root = tmp
        elif nd is not nd.parent.right:
            nd.parent.right = tmp
        else:
            nd.parent.left = tmp
        tmp.right = nd
        nd.parent = tmp
        
    def insert_as_in_BST(self,value):
        node = node_block(value)
        node.left = self.sentinel
        node.right = self.sentinel
        #self.sentinel.parent = node
        node.red = True
        
        tmp = self.root
        bck = None
        while tmp is not self.sentinel:
            bck = tmp
            if node.val > tmp.val:
                tmp = tmp.right
            elif node.val < tmp.val:
                tmp = tmp.left
            else:
                return
            
        node.parent = bck
        if bck is None:
            self.root = node
        elif node.val > bck.val:
            bck.right = node
        else:
            bck.left = node
        self.repair_RB_Tree(node)
        print(self.root.val, " roooooooot")
        self.in_order(self.root)
        print("------------------------------------------------------")
        
    def in_order(self,rt):
        if rt is self.sentinel:
            return
        else:
            self.in_order(rt.right)
            print("node color : ",rt.red,"node val : ",rt.val,", node right : ",rt.right.val,", node left : ",rt.left.val)
            self.in_order(rt.left)
            
    def minimum(self,rt):
        while rt is not self.sentinel:
            bck = rt
            rt = rt.left
        return bck.val
        
    def maximum(self,rt):
        while rt is not self.sentinel:
            bck = rt
            rt = rt.right
        return bck.val
    def successor(self,rt):
        return self.minimum(rt.right)
    def predecessor(self,rt):
        return self.maximum(rt.left)
    def search(self,value):
        tmp = self.root
        while tmp is not self.sentinel:
            if value > tmp.val:
                tmp = tmp.right
            elif value < tmp.val:
                tmp = tmp.left
            else:
                print("found it", tmp.val)
                return
        if tmp is self.sentinel:
            print("number does not exists")
            return
        
        
    
            
        
            
        
        
        
    
        
            
            
        



            
            



#test cases ------------------------------------------------------
tr = Tree()
tr.insert_as_in_BST(20)
tr.insert_as_in_BST(22)
tr.insert_as_in_BST(225)
tr.insert_as_in_BST(15)
tr.insert_as_in_BST(30)
tr.in_order(tr.root)
print(tr.minimum(tr.root))
print(tr.maximum(tr.root))
print(tr.successor(tr.root))
print(tr.predecessor(tr.root.left))
tr.search(500)
                