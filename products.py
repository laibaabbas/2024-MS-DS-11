# 2024-MS-DS-11
def show_products(products):
    print("    pid   name              ...   image                rating") 
    for index, (pid, product) in enumerate(products.items()):
        print(f"{index}   {pid:5} {product['name']:15}   ...  {product['image']:20}  {product['rating']:5}")
    
    print(f"[{len(products)} rows x 6 columns]")

def add_product(products): 
    pid = input("Enter product ID: ")
    name = input("Enter product name: ")
    image = input("Enter image name: ")
    rating = float(input("Enter rating: "))
    products[pid] = {'name': name, 'image': image, 'rating': rating}
    print( [pid, name, image, rating])

def delete_product(products):
    pid = input("Enter product ID to delete or any key to exit :")
    if pid in products:
        del products[pid]
        print("Product deleted successfully!")
    else:
        print("Product not found.")

def update_product_rating(products):
    pid = input("Enter product ID to update rating: ")
    if pid in products:
        new_rating = float(input("Enter new rating: "))
        products[pid]['rating'] = new_rating
        print("Rating updated successfully!")
    else:
        print("Product not found.")

def main():
    products = {
        'p01': {'name': 'Refrigerator', 'image': 'refrigerator.jpg', 'rating': 4.5},
        'p04': {'name': 'Washing Machine', 'image': 'washing_machine.jpg', 'rating': 4.2},
        'p05': {'name': 'Dishwasher', 'image': 'dishwasher.jpg', 'rating': 4.8},
        'p06': {'name': 'Coffee Maker', 'image': 'coffee_maker.jpg', 'rating': 4.3},
        'p07': {'name': 'Toaster', 'image': 'toaster.jpg', 'rating': 4.0},
        'p08': {'name': 'Blender', 'image': 'blender.jpg', 'rating': 4.5},
        'p10': {'name': 'Air Purifier', 'image': 'air_purifier.jpg', 'rating': 4.6},
        'p11': {'name': 'Electric Kettle', 'image': 'electric_kettle.jpg', 'rating': 1.1},
        'p12': {'name': 'New Machine', 'image': 'new_machine.jpg', 'rating': 4.0}
    }

    while True:
        print("1. Show All Products")
        print("2. Add New Product")
        print("3. Delete a Product")
        print("4. Update Product Rating")
        print("5. Exit")
        choice = input("Enter Option to Continue: ")

        if choice == '1':
            show_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            delete_product(products)
        elif choice == '4':
            update_product_rating(products)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()