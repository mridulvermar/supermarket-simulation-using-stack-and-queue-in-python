class Basket:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to Basket") 
    def remove_item(self):
        if self.items:
            item = self.items.pop()
            print(f"{item} removed from Basket")
            return item
        else:
            print("Basket is empty")
            return None
    def view_items(self):
        if self.items:
            print(f"Items in Basket: {self.items[::-1]}")
        else:
            print("Basket is empty")


class CheckoutQueue:
    def __init__(self):
        self.queue = []  
    def enqueue(self, customer):
        self.queue.append(customer)
        print(f"{customer} added to Queue")  
    def dequeue(self):
        if self.queue:
            customer = self.queue.pop(0)
            print(f"{customer} removed from Queue")
            return customer
        else:
            print("Queue is empty")
            return None  
    def view_queue(self):
        if self.queue:
            print(f"Customers in Queue: {self.queue}")
        else:
            print("Queue is empty")


class Supermarket:
    def __init__(self):
        self.baskets = {} 
    def new_customer(self, customer_id):
        self.baskets[customer_id] = Basket()
        print(f"Customer {customer_id} added to Supermarket")  
    def add_item_to_basket(self, customer_id, item):
        if customer_id in self.baskets:
            self.baskets[customer_id].add_item(item)
        else:
            print(f"Customer {customer_id} not found in Supermarket") 
    def remove_item_from_basket(self, customer_id):
        if customer_id in self.baskets:
            return self.baskets[customer_id].remove_item()
        else:
            print(f"Customer {customer_id} not found in Supermarket")  
    def view_basket(self, customer_id):
        if customer_id in self.baskets:
            self.baskets[customer_id].view_items()
        else:
            print(f"Customer {customer_id} not found in Supermarket")  
    def checkout_customer(self, customer_id):
        if customer_id in self.baskets:
            del self.baskets[customer_id]
            print(f"Customer {customer_id} checked out and removed from Supermarket")
        else:
            print(f"Customer {customer_id} not found in Supermarket")

if __name__ == "__main__":
    supermarket = Supermarket()
    checkout_queue = CheckoutQueue()
    customer_id = 1   
    while True:
        print("\nWelcome to the Supermarket")
        print("1. Add Customer")
        print("2. Add Item to Basket")
        print("3. Remove Item from Basket")
        print("4. View Basket")
        print("5. View Queue")
        print("6. Checkout")
        print("7. Exit")     
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice, please enter a number between 1 and 7")
            continue     
        if choice == 1:
            supermarket.new_customer(customer_id)
            customer_id += 1
        elif choice == 2:
            try:
                cust_id = int(input("Enter customer ID: "))
                item = input("Enter item to add: ")
                supermarket.add_item_to_basket(cust_id, item)

            except ValueError:
                print("Invalid customer ID")
        elif choice == 3:
            try:
                cust_id = int(input("Enter customer ID: "))
                supermarket.remove_item_from_basket(cust_id)
            except ValueError:
                print("Invalid customer ID")
        elif choice == 4:
            try:
                cust_id = int(input("Enter customer ID: "))
                supermarket.view_basket(cust_id)
            except ValueError:
                print("Invalid customer ID")
        elif choice == 5:
            checkout_queue.view_queue()
        elif choice == 6:
            try:
                cust_id = int(input("Enter customer ID: "))
                checkout_queue.enqueue(cust_id)
                supermarket.checkout_customer(cust_id)
            except ValueError:
                print("Invalid customer ID")
        elif choice == 7:
            break
        else:
            print("Invalid choice, please enter a number between 1 and 7") 
