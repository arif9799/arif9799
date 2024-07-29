
import re

strii = "My name is Arif. My last name is WB."
lstt = re.findall(r'[a-z]+', strii.lower())

class node_block:
    def __init__(self,word,count):
        self.word = word
        self.count = count
        self.nxt_node = None

class lists:
    def __init__(self):
        self.first = None
        self.current = None
        
    def insert_values(self,word):
        if self.first is None :
            node = node_block(word,1)
            self.first = node
            self.current = node
        else : 
            flag = 0
            tmp = self.first
            while tmp is not None:
                if tmp.word == word:
                    tmp.count = tmp.count + 1 #equivalent to increase function
                    flag = 1
                    break
                else : 
                    tmp = tmp.nxt_node
            if flag == 0:
                node = node_block(word,1)
                self.current.nxt_node = node
                self.current = node
                
    def delete_values(self,word):
        tmp = self.first
        bck = None
        while tmp is not None:
            
            if tmp.word == word:
                break
            else:
                bck = tmp
                tmp = tmp.nxt_node
            
        if tmp is None:
            print("Word does not exists")
        else:
            if tmp is self.first:
                print(self.first.word,"---deleted")
                self.first = self.first.nxt_node
                
            else:
                print(tmp.word,"---deleted")
                bck.nxt_node = tmp.nxt_node
            
    def search_value(self,word):
        tmp = self.first
        while tmp is not None:
            if tmp.word == word:
                print("Found it - ", tmp.word," - ",tmp.count)
                break
            else:
                tmp = tmp.nxt_node
        if tmp is None:
            print("the word does not exist")
            
        
        
    def count(self):
        i=0
        tmp = self.first
        while tmp is not None:
            i+=1
            tmp = tmp.nxt_node
        return i
        
    def print_list(self):
        tmp = self.first
        while tmp is not None:
            print(tmp.word," - ",tmp.count)
            tmp = tmp.nxt_node
        print("------------------------------------------------------------")

L = [None] * 10
for i in range(10):
    L[i] = lists()

#converting character into numeric
def convert_to_int(st):
    temp = 0
    for i in st:
        temp = temp + ord(i)
    return temp

#hash functions  
def hash_func(val):
    return val%10
    
#calling the list class's function insert_values
def insert_in_table(loc,word):
    L[loc].insert_values(word)
    
#calling the list class's function delete_values
def delete_from_table(loc,word):
    L[loc].delete_values(word)
    
#calling the list class's function search_value
def search_from_table(loc,word):
    L[loc].search_value(word)
    


#test cases ----- inserting all the words
for word in lstt:
    insert_in_table(hash_func(convert_to_int(word)),word)
search_from_table(hash_func(convert_to_int("arif")),"arif")
delete_from_table(hash_func(convert_to_int("arif")),"arif")
search_from_table(hash_func(convert_to_int("arif")),"arif")
for i in L:
    print(i.print_list())  
 

     
        
        