class Tree:
    def __init__(self,val=None): # __init__ method to handle initialization with arguments t = Tree(40) #create a tree value with root value 40
                                # Ex:TypeError: Tree() takes no arguments

        self.value = val #initialize the tree node with a value 

        if self.value: #If the node has a value, create left and right children nodes
            self.left = Tree()
            self.right = Tree()
            
        else: # If the node has no value,set left and right children to None
            self.left = None
            self.right = None

    def isempty(self): #check if the node is empty
        return(self.value == None)

    def insert(self,data): #insert data into tree

        if self.isempty(): #if the node is empty, insert data here
            self.value = data


            self.left = Tree() #create left and right children for the inserted node
            self.right = Tree()
            print("{} is inserted successfully".format(self.value))

        elif data < self.value: # If data is less than current node value,insert into left subtree
                self.left.insert(data)
                return

        elif data > self.value: # If data is greater than current node value,insert into right subtree
                self.right.insert(data)

        elif data == self.value: # Nothing to do If data is equal to current node value
            return

t = Tree(40) #create a tree value with root value 40

t.insert(55)# insertion of some values
t.insert(10)
t.insert(18)
t.insert(2)

            
            
            
