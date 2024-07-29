import math
import random

class node_block:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.down = None
        self.up = None
        self.val = value
        
        
class skiplists:
    
    def __init__(self):
        head_node = node_block(-math.inf)
        tail_node = node_block(math.inf)
        self.head = head_node
        self.tail = tail_node
        
    def insert_in_SL(self,val):
        
        if self.head.right is None:
            node = node_block(val)
            self.head.right = node
            node.left = self.head
            node.right = self.tail
            return node
        else:
            tmp = self.head
            while val > tmp.val:
                bck = tmp
                tmp = tmp.right
            node = node_block(val)
            bck.right = node
            node.left = bck
            node.right = tmp
            return node
        
    def print_list(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.right    
        
        

L = list()
L.append('')
L[0] = skiplists()
def insert(val):
    i = 1
    nd = L[0].insert_in_SL(val)
    nd.down = None
    while random.randrange(0,2) != 0:
        if i+1 > len(L):
            L.append('')
            L[i] = skiplists()
            L[i-1].head.up = L[i].head
            L[i].head.down = L[i-1].head
            L[i-1].tail.up = L[i].tail
            L[i].tail.down = L[i-1].tail
        nd.up = L[i].insert_in_SL(val)
        nd.up.down = nd
        nd = nd.up
        i = i + 1

def lookup(node_arg,val):
    if val == node_arg.val:
        return node_arg
    elif node_arg.val == math.inf:
        return
    else:
        if node_arg.down is not None:
            if val > node_arg.val and val < node_arg.down.right.val:
                return lookup(node_arg.down,val)
            elif val > node_arg.val and val >= node_arg.down.right.val:
                return lookup(node_arg.down.right,val)
        else:
            if (val > node_arg.val and val < node_arg.right.val) or (val < node_arg.val and val > node_arg.right.val):
                return None
            else:
                if val > node_arg.val:
                    return lookup(node_arg.right,val)
                else:
                    return lookup(node_arg.left,val)
                

def delete(val):
    tmp = lookup(L[len(L)-1].head,val)
    if tmp is None:
        print("No such element exists")
    else:
        print("it does")
        pass
    
            



#||||||||||test cases||||||||||

insert(10) 
insert(20)
insert(40) 
insert(30) 
insert(50)
insert(60)
insert(80)
ndtmp = lookup(L[len(L)-1].head,10)
if ndtmp is None:
    print("not found")
else:
    print("found",ndtmp.val)
    
delete(10)


print(L[len(L)-1].head.right.val)
jst = L[len(L)-1].head.right
for i in range(len(L),1,-1):
    print(jst.val)
    jst = jst.down
print(jst.right.val)
for i in L:
    print(i.count())
    i.print_list()
    