import os


class CRUDApplication:
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        self.item_list.append(item)
        print(f"Item '{item}' added successfully.")

    def update_item(self, index, new_item):
        if index >= 0 and index < len(self.item_list):
            self.item_list[index] = new_item
            print(f"Item at index {index} updated successfully.")
        else:
            print("Invalid index.")

    def delete_item(self, index):
        if index >= 0 and index < len(self.item_list):
            deleted_item = self.item_list.pop(index)
            print(f"Item '{deleted_item}' deleted successfully.")
        else:
            print("Invalid index.")

    def display_items(self):
        if not self.item_list:
            print("No items to display.")
            return

        print("Current items:")
        print("-" * 30)
        print("| Index | Item")
        print("-" * 30)
        for index, item in enumerate(self.item_list):
            print(f"| {index:^6} | {item:<20}")
        print("-" * 30)


def display_initial_load():
    clear_console()
    print("""            
                                      &                                         
                                     #%@                                        
                                      %#                                        
                                @#%&&&%&&&&&&                                   
                   &%&@   #@%&@#     ,%%     %&&&@,    %&@                      
                        @*           @%@            @                           
                       & /           @&@           @ &                          
                      &   #          @%@          @   &                         
                     &     &         @&@         &     @                        
                    %       &        @&@        &       &                       
                   (.        &       &&@       &         (                      
                   ,          &      &&@      &.         ,/                     
                  #            %     &&@     (,           /                     
                 &                   /&/    .*             &                    
                 &%%%%%%%%%%%%%&#   %&&&@   %%%%%%%%%%%%%%%@*                   
                     ./&@&#*        %&%&(        ,%@@&/,                        
                                     #&&                                        
                                   &%%&%&%                                      
                               @%%%&&&&&%&&%%%                                
    """)

    print("Welcome to the Laws and Justice application!")
    print("This application allows you to manage laws and legal information.")
    print("You can perform various operations such as adding, updating, deleting, and displaying laws.")
    print()


def clear_console():
    if os.name == "nt":  # for Windows
        os.system("cls")
    else:  # for Linux and Mac
        os.system("clear")


if __name__ == "__main__":
    app = CRUDApplication()
    display_initial_load()

    while True:
        print("Select an option:")
        print("1. Add law")
        print("2. Update law")
        print("3. Delete law")
        print("4. Display laws")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            law = input("Enter the law to add: ")
            app.add_item(law)
        elif choice == "2":
            index = int(input("Enter the index of the law to update: "))
            new_law = input("Enter the new law: ")
            app.update_item(index, new_law)
        elif choice == "3":
            index = int(input("Enter the index of the law to delete: "))
            app.delete_item(index)
        elif choice == "4":
            app.display_items()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-5).")
