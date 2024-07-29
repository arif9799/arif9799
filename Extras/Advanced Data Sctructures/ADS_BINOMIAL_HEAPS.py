import math

class node:
    def __init__(self,value):
        self.left_child = None
        self.right_sibling = None
        self.parent = None
        self.degree = 0
        self.key = value
        
class Binomial_heap:
    def __init__(self):
        self.head = None
    
    
    def insert1(self,val):
        tmp_heap = self.Make_Heap()
        nd = node(val)
        tmp_heap.head = nd 
        if self.head is None: 
            self.head = nd
            return self
        else:
            return self.UNION(tmp_heap)
            
    def BINOMIAL_LINK(self,y,z):
        y.parent = z
        y.right_sibling = z.left_child
        z.left_child = y
        z.degree = z.degree + 1

    def Make_Heap(self):
        return Binomial_heap()    
    
    def UNION(self,tmp_heap):
        new_heap = self.Make_Heap()
        new_heap.head = self.MERGE(tmp_heap)

        if new_heap.head is None:
            return new_heap
        prev_x = None
        x = new_heap.head
        next_x = x.right_sibling
        #new_heap.printall()
        
        while next_x is not None:
            if (x.degree != next_x.degree) or ((next_x.right_sibling is not None) and (next_x.right_sibling.degree == x.degree)):
                prev_x = x 
                x = next_x
            elif x.key <= next_x.key:
                x.right_sibling = next_x.right_sibling
                self.BINOMIAL_LINK(next_x,x)
            elif prev_x is None:
                x = next_x
                #print(new_heap.head.key,"--",new_heap.head.degree,"second else")
            else:
                prev_x.right_sibling = next_x
                self.BINOMIAL_LINK(x,next_x)
                x = next_x
            next_x = x.right_sibling
        return new_heap
        
        
    def MERGE(self,tmp_heap):
        
        htr = self.Make_Heap()
        htr = tmp_heap
        tmp = htr.head
        bck = None
        while tmp is not None:
            bck = tmp
            tmp = tmp.right_sibling
        bck.right_sibling = self.head
        cnt = htr.count()
        for i in range(cnt):
            if htr.head.degree > htr.head.right_sibling.degree:
                tp = htr.head.right_sibling
                htr.head.right_sibling = tp.right_sibling
                tp.right_sibling = htr.head
                htr.head = tp
            prev = None
            x = htr.head
            next = htr.head.right_sibling
            while next is not None:
                if x.degree > next.degree and prev is not None:
                    prev.right_sibling = next 
                    x.right_sibling = next.right_sibling
                    next.right_sibling = x
                prev = x
                x = next 
                next = next.right_sibling
        return htr.head            

    def count(self):
        i=0
        tmp = self.head
        while tmp is not None:
            i+=1
            tmp = tmp.right_sibling
        return i 
        
    def extract_min(self):
        minnode = self.head
        tmp = self.head
        bck = None
        prev = tmp
        while tmp is not None:
            if tmp.key < minnode.key:
                prev = bck
                minnode = tmp
            bck = tmp
            tmp = tmp.right_sibling
        prev.right_sibling = minnode.right_sibling
        
        tmp_heap = self.Make_Heap()
        tmp_heap.head = minnode.left_child
        L = []
        tmp = tmp_heap.head
        while tmp is not None:
            L.append(tmp)
            tmp = tmp.right_sibling
        L.reverse()
        for i in range(len(L)):
            if i == (len(L)-1):
                L[i].right_sibling = None
                break
            L[i].right_sibling = L[i+1]
        tmp_heap.head = L[0]
        tmp_heap.printall()
        return self.UNION(tmp_heap)
        
    def minimum(self):
        minnode = self.head
        tmp = self.head
        while tmp is not None:
            if tmp.key < minnode.key:
                minnode = tmp
            tmp = tmp.right_sibling
        print(minnode.key,"success")
        
        
    def printall(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.key,"||||")
            tmp = tmp.right_sibling
    
    def decrease_key(self,nd,key_dec):
        if key_dec > nd.key:
            print("error, not possible")
            return
        nd.key = key_dec
        y = nd
        z = y.parent
        while (z is not None) and (y.key < z.key):
            z.key,y.key = y.key,z.key
            
            y,z = z,y
            y = z
            z = y.parent
            
            
        
    def delete(self,nd):
        self.decrease_key(nd,-math.inf)
        return self.extract_min()
        




if __name__ == "__main__":
    
    
    H = Binomial_heap()
    H = H.insert1(10)
    H = H.insert1(20)
    H = H.insert1(30)
    H = H.insert1(40)
    H = H.insert1(50)
    H = H.insert1(60)
    H = H.insert1(70)
    H = H.insert1(80)
    H = H.insert1(90)
    
    
    
    H.minimum()
    H.printall()
    print("22222222222222222")
    H = H.extract_min()
    print("22222222222222222")
    H.printall()
    print(H.head.left_child.key)
    H.decrease_key(H.head.left_child.left_child,15)
    print(H.head.key)
    print(H.head.left_child.key)
    print(H.head.left_child.left_child.key)
    H = H.delete(H.head)
    print(H.head.key)
    
    
    
    
    
    
    
    
       