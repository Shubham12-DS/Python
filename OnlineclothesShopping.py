# ----------------------------------------------------------------------
# A Simple Console-Based Clothes Shopping Application
# This application allows a user to browse products, add them to a cart,
# view the cart, and see the total cost.
# ----------------------------------------------------------------------

import time

# --- 1. Product Class ---

class Product:
    """
    A blueprint for a single clothing item.
    It holds essential details like name, price, and stock count.
    """
    def __init__(self, item_id, name, category, price, stock):
        self.id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def __str__(self):
        """Returns a human-readable string representation of the product."""
        return f"{self.id}. {self.name} ({self.category}) - ${self.price:.2f} (In Stock: {self.stock})"

# --- 2. ShoppingCart Class ---

class ShoppingCart:
    """
    Manages the user's cart. It keeps track of the items added and their quantities.
    """
    def __init__(self):
        # The cart is a dictionary mapping Product objects to quantities (integers)
        self.items = {}

    def add_item(self, product, quantity):
        """Adds a product to the cart or updates its quantity."""
        if product.stock < quantity:
            print(f"\n🚫 Sorry, only {product.stock} of '{product.name}' are available.")
            return

        # If the product is already in the cart, increase the quantity
        if product in self.items:
            self.items[product] += quantity
        else:
            # Otherwise, add it to the cart
            self.items[product] = quantity

        product.stock -= quantity
        print(f"\n🛒 Added {quantity} x '{product.name}' to your cart!")

    def view_details(self):
        """Displays all items currently in the cart with their subtotals."""
        if not self.items:
            print("\nYour shopping cart is currently empty. Time to find some new clothes!")
            return 0.0

        print("\n--- Your Shopping Cart ---")
        total_cost = 0.0

        # Loop through each product and its quantity in the cart
        for product, quantity in self.items.items():
            subtotal = product.price * quantity
            total_cost += subtotal
            print(f"- {product.name.ljust(25)} x {str(quantity).ljust(2)} @ ${product.price:.2f} = ${subtotal:.2f}")

        return total_cost

    def calculate_total(self):
        """Calculates and returns the grand total of the cart."""
        total = self.view_details()
        print("-" * 30)
        print(f"Grand Total: ${total:.2f}")
        print("-" * 30)
        return total

# --- 3. Main Application Class ---

class ShoppingApp:
    """
    The main engine for the shopping experience, handling data and user interaction.
    """
    def __init__(self):
        self.products = self._load_products()
        self.cart = ShoppingCart()
        self.is_running = True

    def _load_products(self):
        """Initializes the inventory of clothes."""
        print("👕👖 Loading the fashion inventory...")
        time.sleep(1) # Added for a human touch
        
        # Dictionary to store products, mapping ID (int) to Product object
        inventory = {
            1: Product(1, "Classic Denim Jeans", "Bottoms", 49.99, 15),
            2: Product(2, "Oversized Knit Sweater", "Tops", 34.50, 8),
            3: Product(3, "Leather Biker Jacket", "Outerwear", 129.99, 4),
            4: Product(4, "Striped Cotton T-Shirt", "Tops", 19.99, 25),
            5: Product(5, "Wool Scarf (Navy)", "Accessories", 15.00, 30)
        }
        return inventory

    def _display_menu(self):
        """Shows the main options to the user."""
        print("\n" + "="*40)
        print("👗 Welcome to the Console Clothing Boutique 🛍️")
        print("="*40)
        print("1. Browse Products")
        print("2. Add Item to Cart")
        print("3. View Shopping Cart & Total")
        print("4. Checkout (View Final Total & Exit)")
        print("5. Exit Application")
        print("="*40)
        
    def browse_products(self):
        """Displays all available products from the inventory."""
        print("\n--- Available Inventory ---")
        for product in self.products.values():
            if product.stock > 0:
                print(product)
        print("---------------------------\n")

    def add_item_to_cart(self):
        """Guides the user through selecting a product and quantity to add."""
        self.browse_products()

        try:
            choice_id = int(input("Enter the ID of the item you want to buy (or 0 to cancel): "))
            if choice_id == 0:
                return

            if choice_id not in self.products:
                print("❌ Invalid product ID. Please try again.")
                return

            selected_product = self.products[choice_id]

            if selected_product.stock <= 0:
                 print(f"⚠️ '{selected_product.name}' is currently out of stock.")
                 return

            quantity = int(input(f"How many '{selected_product.name}' would you like to add? (Max {selected_product.stock}): "))

            if quantity <= 0:
                print("🤔 Quantity must be 1 or more.")
                return

            # Delegate the actual adding logic to the ShoppingCart
            self.cart.add_item(selected_product, quantity)

        except ValueError:
            print("❌ Invalid input. Please enter a number for the ID and quantity.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def checkout(self):
        """Finalizes the shopping session."""
        print("\n🎉 Thank you for shopping with us!")
        final_total = self.cart.calculate_total()
        if final_total > 0:
            print("Your order has been placed. Payment processed.")
        print("Goodbye! Come back soon for more great fashion.")
        self.is_running = False

    def run(self):
        """The main execution loop of the application."""
        while self.is_running:
            self._display_menu()
            
            try:
                choice = input("Enter your choice (1-5): ")
                
                if choice == '1':
                    self.browse_products()
                elif choice == '2':
                    self.add_item_to_cart()
                elif choice == '3':
                    self.cart.calculate_total()
                elif choice == '4':
                    self.checkout()
                elif choice == '5':
                    print("\nExiting application. Your cart will not be saved.")
                    self.is_running = False
                else:
                    print("🚫 Invalid choice. Please select a number from 1 to 5.")
                    
            except KeyboardInterrupt:
                print("\n\nApplication interrupted by user. Exiting gracefully.")
                self.is_running = False
            except Exception as e:
                print(f"An unexpected system error occurred: {e}")
                
# --- 4. Execution Block ---

if __name__ == "__main__":
    app = ShoppingApp()
    app.run()
    
