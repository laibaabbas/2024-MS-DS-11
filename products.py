products = [
    {"pid": "p01", "name": "Refrigerator", "image": "refrigerator.jpg", "rating": 4.5},
    {"pid": "p04", "name": "Washing Machine", "image": "washing_machine.jpg", "rating": 4.2},
    {"pid": "p05", "name": "Dishwasher", "image": "dishwasher.jpg", "rating": 4.8},
    {"pid": "p06", "name": "Coffee Maker", "image": "coffee_maker.jpg", "rating": 4.3},
    {"pid": "p07", "name": "Toaster", "image": "toaster.jpg", "rating": 4.0},
    {"pid": "p08", "name": "Blender", "image": "blender.jpg", "rating": 4.5},
    {"pid": "p10", "name": "Air Purifier", "image": "air_purifier.jpg", "rating": 4.6},
    {"pid": "p11", "name": "Electric Kettle", "image": "electric_kettle.jpg", "rating": 4.1},
    {"pid": "p12", "name": "new machine", "image": "new_machine.jpg", "rating": 4.0},
]

# Function to show all products in tabular format
def show_products(products):
    for index, product in enumerate(products):
        print( index, product['pid'], product['name'], product['image'], product['rating'])
    
    print("\n[", len(products), " rows x 4 columns]\n" )

# Function to add a new product
def add_product(products):
    pid = input("Enter Product id: ")
    name = input("Enter Product name: ")
    image = input("Enter Product image: ")
    rating = float(input("Enter Product Rating: "))
    
    # Adding the product to the dictionary
    products[pid] = {"name": name, "image": image, "rating": rating}
    
    print("\nNew product added:", [pid, name, image, rating])

# Function to delete a product
def delete_product(products):
    show_products(products)
    pid = input("Enter the product id to delete or any key to exit ")
    
    if pid in products:
        del products[pid]
        print("\nProduct deleted successfully!")
    else:
        print("\nInvalid product id.")

# Function to update product rating
def update_rating(products):
    show_products(products)
    pid = input("Enter the product id to update the rating: ")
    
    if pid in products:
        new_rating = float(input("Enter new rating for %s: " % products[pid]['name']))
        products[pid]['rating'] = new_rating
        print("\nRating updated successfully!")
    else:
        print("\nInvalid product id.")

# Main function for the CRUD operations
def main():

    while True:
        print("\n1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        option = int(input("Enter Option to Continue: "))

        if option == 1:
            show_products(products)
        elif option == 2:
            add_product(products)
        elif option == 3:
            delete_product(products)
        elif option == 4:
            update_rating(products)
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
