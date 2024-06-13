class BinarySearchTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self,data):
        if self.data == data:
            return
        if self.data > data :
            #Assign to left Search tree
            if self.left : #Child exists  in left subtree
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)#Add left child node
        else: #Assign to right search tree
            if self.right : #Child exists  in right subtree
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)#Add left child node
    def in_order_traversal(self):
        #in order traversal
        #First left tree
        # then root node
        #Then right tree
        elements = []
        #Left
        if self.left:
            elements +=self.left.in_order_traversal()
        #Base
        elements.append(self.data)
        #right traversal
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements
    def search(self,val):

        if self.data == val:
            #Exact match found
            return True
        elif self.data > val:
            #search in left search tree
            if self.left:
                
                return  self.left.search(val)

            else:
                return False #Nothing found
        else:
            #search in left search tree
            if self.right:
                
                return  self.right.search(val)

            else:
                return False #Nothing found

#Helper method
def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for itr in range(1,len(elements)):
        root.add_child(elements[itr])
    return root



if __name__ =='__main__':
    elements = [17,5,6,24]
    numbers_tree = build_tree(elements)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(25))
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    

                


            
