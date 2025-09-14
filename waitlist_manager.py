# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    
    



# Create a LinkedList class to manage the waitlist
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
    
    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def remove(self, name):
        current = self.head
        prev = None
        
        while current:
            if current.name == name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
        
    def print_list(self):
        current = self.head
        while current:
            print(current.name)
            current = current.next
            print("NONE")
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)
            print(f"{name}add to front of the list")

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)
            print(f"{name} added to end of the list")

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            waitlist.remove(name)
            print(f"{name} removed from the list")
            
        elif choice == "4":
            print("Current waitlist:")
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
            

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")

# Call the waitlist_generator function to start the program
waitlist_generator()

'''
#This program, known as the waitlist manager, uses a linked list to manage the names of customers. These "customers" are represented by something called a node, which stores their names in the list. My list class keeps track of everything through pointers, which refer to the nodes. The order of everything follows each node from start to end, like adding a customer, adding a customer to the end, removing a customer, printing the list, and exiting.
#The head is the starting point of the list; if the list is empty, the head is set to "None". When a new customer is added to my list, the head gets updated to a new node. The head allows us to keep track of the first customer, and from there, we can follow everything else in our list.
#A real engineer may need a list like this when dealing with a lot of removing/deleting a bunch of things quite often. They may also use a list like this when dealing with dynamic data that may change often, or when the size of everything is unknown. I do know a resturant manager could use this system to manage their customer waitlists effectively and quickly.

'''
