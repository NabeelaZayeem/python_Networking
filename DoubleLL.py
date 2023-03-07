import sys

class Node:
    def _init_(self):
        self.prev = None

        self.data = input("Enter data of the new node")
        self.next = None

class DoublyList:
    def _init_(self,first,last):
        self.first = None
        self.last = None
        print("An empty doubly LL is created")

    def insertFront(self):
        nn = Node() # create a new node object
        if self.first == None:  # if list is empty
            self.first = self.last = nn
            return
        self.first.prev = nn  # make the 1st node in list point to new node
        nn.next = self.first  # make the new node point to 1st node in list
        self.first = nn  # make the new node as 1st node

    def insertRear(self):
        nn = Node()
        if self. first == None:  # if list is empty
            self.first = self.last = nn
            return
        self.last.next = nn  # make the last node point to the new node
        nn.prev = self.last  # make the new node point to last node
        self.last = nn  # make the new node as last node

    def deleteNode(self):
        if self.first == None:
            print("List is empty")
            return
        userData = input("Enter data of the node to be deleted: ")
        if self.first == self.last:  # if list has only one node
            if self.first.data == userData:
                print("Node with data ", userData, " is deleted ")
                self.first = self.last = None  # make the list empty
                return
            print("Node with data ", userData, " was not found")
        else:  # list has 2 or more nodes
            temp = self.first
            while temp.data != userData and temp != self.last:
                temp = temp.next
            if temp.data == userData:  # we found the node to be deleted
                print("Node with data ", userData, " is deleted")
                if temp == self.first:  # node to be deleted is 1st node
                    self.first = first.next  # make the 2nd node as 1st node
                    self.first.prev = None
                elif temp == self.last:  # node to be deleted is last node
                    self.last = self.last.prev  # make the last but node as last node
                    self.last.next = None
                else:  # node to be deleted is inbetween node
                    temp.prev.next = temp.next  # make prev node of temp point to its next node
                    temp.next.prev = temp.prev  # make next node of temp point to its prev node
            else:
                print("Node with data ", userData, " was not found")

    def display_list(self):
        if self.first == None:
            print("List is empty")
            return
        temp = self.last  # begin from the rear end
        print("List elements from rear to front are")
        while temp != None:  # unitl temp has not reached prev link of 1st node
            print(temp.data)
            temp = temp.prev


def invalid_choice():
    print("Invalid operation")


obj = DoublyList()  # created an object of the class
choice = 0
list_operations = {
    1: obj.insertFront,
    2: obj.insertRear,
    3: obj.deleteNode,
    4: obj.display_list,
    5: sys.exit
}

while True:
    print("1:InsertFront 2: InsertRear 3:DeleteNode 4:Display List 5:Exit ")
    choice = int(input("Your choice ? "))
    list_operations.get(choice, invalid_choice)()

