class new_node:
    def input_data(self):
        self._data = input("Enter Data : ")
        self._pref = None
        self._nref = None


class linked_list(new_node):
    def __init__(self):
        self.__head = None

#ADDING ELEMENT AT THE ENDING
    def add_at_end(self):
        new = new_node()    #NEW linked list is created
        new.input_data()
        if self.__head is None: #if linked list is empty
            self.__head = new   #putting linked list address in head or adding first node

        elif self.__head is not None:#if liked list is not empty or adding send node
            n = self.__head #putting the address of first linked list in variable n
            while(n._nref != None): # traverising the linked list upto the None
                n = n._nref
            n._nref = new       #Adding the linked list
            new._pref = n       #at the end of the linked list
        else:
            pass

#adding element in the starting
    def add_at_beginning(self):
        new = new_node()
        if (self.__head is None):
            print("Linked list is empty")
        else:
            new.input_data()
            new._nref = self.__head
            self.__head._pref = new
            self.__head = new



# Traversing the linkded list
#in forward direction

    def traverse_in_frwd(self):
        if (self.__head is None):
            print("Linked list is empty")
        else:
            print("Traversing the linked list in forward direction ")
            n = self.__head
            while n is not None:
                if(n._nref is not None):
                        print(n._data,"-->",end="")
                        n = n._nref
                else:
                    print(n._data)
                    n = n._nref

    def traverse_in_bcwd(self):
        if (self.__head is None):
            print("Linked list is empty")
        else:
            print("\nTraversing the linked list in backward direction direction ")
            n = self.__head
            while (n._nref is not None):
                n = n._nref
            while (n is not None):
                if (n._pref is not None):
                    print(n._data,"-->",end="")
                    n = n._pref
                else:
                    print(n._data)
                    n = n._pref


#add linked list after a element
    def add_after(self):
        if (self.__head == None):
            print("Linked List is empty")
        elif (self.__head != None):
            element = input("After which element you want to enter :  ")
            new = new_node()
            new.input_data()
            n = self.__head
            z = False
            while(n != None):
                if(n._data == element):
                    z = True
                    break
                n=n._nref
            if(z==True):
                if (n._nref == None):
                    new._pref = n
                    n._nref = new
                elif (n._nref is not None):
                    new._pref = n
                    new._nref = n._nref
                    n._nref._pref = new
                    n._nref = new
            else:
                print("element does not exist")


#add linked list before a element
    def add_before(self):
        if (self.__head == None):
            print("Linked List is empty")
        elif (self.__head != None):
            element = input("Before which element you want to enter :  ")
            new = new_node()
            new.input_data()
            n = self.__head
            z = False
            while(n != None):
                if(n._data == element):
                    z = True
                    break
                n=n._nref
            if(z==True):
                if (n._pref == None):
                    new._nref = n
                    n._pref = new
                    self.__head = new
                else:
                    new._nref = n
                    new._pref = n._pref
                    n._pref._nref = new
                    n._pref = new
            else:
                print("Element doesn't exist")


#delete from the beginning
    def del_beggening(self):
        if (self.__head is None):
            print("Linked List Is Empty")
            return
        if (self.__head._nref is None):
            print("DLL having only one LL and deleted LL is ",self.__head._data)
            self.__head = None
            return
        if (self.__head._nref is not None):
            print("DLL having more then one LL and deleted LL is ", self.__head._data)
            self.__head = self.__head._nref
            self.__head._pref = None
            return


##delete linked list from the ending
    def del_at_end(self):
        if (self.__head is None):
            print("Linked List is empty")
            return
        if (self.__head._nref is None):
            print("DLL having only one LL and deleted LL is ", self.__head._data)
            self.__head = None
            return

        if (self.__head is not None):
            n = self.__head
            while (n._nref is not None):
                n = n._nref
            print("Last node containing data {0} have been deleted".format(n._data))
            n._pref._nref = None
            del n


#delete by position
    def del_by_val(self):
#if no node is present
        if (self.__head is None):
            print("Linked list is empty")
            return
#only single node is present
        elif(self.__head._nref == None):
            __d_data = input("Enter Data to delete : ")
            if(self.__head._data == __d_data):
                self.__head = None
            else:
                print("Data is not present in the linked list")
            return

#if more then 1 node is present
        elif(self.__head._nref is not None):
            __d_data = input("Enter Data to delete : ")
#and want to delete first node
            if(self.__head._data == __d_data):
                print("Deleting the data {}".format(__d_data))
                self.__head = self.__head._nref
                self.__head._pref = None
                return
            else:
                n = self.__head
                while(n._nref is not None):
                    if(n._data == __d_data):
                        break
                    n = n._nref

                if(n._nref is not None):
                    n._nref._pref = n._pref
                    n._pref._nref = n._nref
                    del n
                    return
                else:
                    if(n._data == __d_data):
                        n._pref._nref = None
                        del n
                        return
                    else:
                        print("data not found")



ll = linked_list()
while(True):
    print("\n\n1]. Add Element")
    print("2]. Add Element At the Last")
    print("3]. Add element at the beginning")
    print("4]. Add element after a element")
    print("5]. Add element before the element")
    print("6]. Delete from Starting")
    print("7]. Delete from Last")
    print("8]. Delete by value")
    print("9]. Traverse linked list i forward direction")
    print("10]. Traverse linked list in backward direction")
    print("0]. enter zero to exit..")
    ch = input("\nEnter your choice : ")
    if(ch=='1'):
        ll.add_at_end()
    elif(ch=='2'):
        ll.add_at_end()
    elif(ch=='3'):
        ll.add_at_beginning()
    elif(ch=='4'):
        ll.add_after()
    elif(ch=='5'):
        ll.add_before()
    elif(ch=='6'):
        ll.del_beggening()
    elif(ch=='7'):
        ll.del_at_end()
    elif(ch=='8'):
        ll.del_by_val()
    elif(ch=='9'):
        ll.traverse_in_frwd()
    elif(ch=='10'):
        ll.traverse_in_bcwd()
    elif(ch=='0'):
        print("You have exited from the game")
        break
    else:
        print("\nWrong Input......")
        input("Press enter to continue.....")
        continue
    con = input("Do u want to continue press (y/Y)")
    if(con in "yY"):
        continue
    else:
        break




'''
ll1 = linked_list()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.add_at_end()
ll1.traverse_in_frwd()
ll1.del_by_val()
ll1.traverse_in_frwd()
ll1.del_by_val()
ll1.traverse_in_frwd()
ll1.del_by_val()
ll1.traverse_in_frwd()
ll1.del_by_val()
ll1.traverse_in_frwd()
ll1.del_by_val()
ll1.traverse_in_frwd()
'''


'''
dll = linked_list()
dll.add_at_end()
dll.add_at_end()
dll.add_at_end()
dll.traverse_in_frwd()
dll.del_at_end()
dll.traverse_in_frwd()
dll.del_at_end()
dll.traverse_in_frwd()
dll.del_at_end()
dll.traverse_in_frwd()
'''



'''
ll = linked_list()
ll.add_at_end()
ll.add_at_end()
ll.traverse_in_frwd()
ll.del_beggening()
ll.traverse_in_frwd()
ll.add_at_end()
ll.add_at_end()
ll.at_beginning()
ll.traverse_in_frwd()
ll.add_after()
ll.traverse_in_frwd()
ll.add_before()
ll.traverse_in_frwd()
ll.traverse_in_bcwd()
'''













