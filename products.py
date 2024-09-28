import csv

# Load products from a CSV file
def load_products_from_csv(file_name="products.csv"):
    products = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['rating'] = float(row['rating'])  # Convert rating to float
                products.append(row)
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with an empty product list.")
    return products

# Save products to a CSV file automatically after any CRUD operation
def update_csv(products, file_name="products.csv"):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ["pid", "name", "image", "rating"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

# Show all products
def show_products(products):
    print("\nList of Products:")
    for index, product in enumerate(products):
        print(  index, product['pid'], product['name'], '...', product['image'], product['rating'])
#   print(f"{index}   {product['pid']}     {product['name']}     ...      {product['image']}    {product['rating']}")
    num_rows = len(products)
    num_columns = 6  # pid, name, description, price, image, rating
    print(f"\n[{num_rows} rows x {num_columns} columns]\n")


# Add a new product and update the CSV
def add_product(products):
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    image = input("Enter Product Image: ")
    rating = float(input("Enter Product Rating: "))
    new_product = {"pid": pid, "name": name, "image": image, "rating": rating}
    products.append(new_product)
    update_csv(products)
    print( list(new_product.values()))

# Delete a product and update the CSV
def delete_product(products):
    show_products(products)
    product_index = int(input("Enter the index of the product to delete or other key to Exit "))
    if 0 <= product_index < len(products):
        del products[product_index]
        update_csv(products)
        print("Product deleted and CSV file updated successfully!")
    else:
        print("Invalid index.")

# Update product rating and update the CSV
def update_rating(products):
    show_products(products)
    product_index = int(input("Enter the index of the product to update the rating: "))
    if 0 <= product_index < len(products):
        new_rating = float(input(f"Enter new rating for {products[product_index]['name']}: "))
        products[product_index]["rating"] = new_rating
        update_csv(products)
        print("Rating updated and CSV file updated successfully!")
    else:
        print("Invalid index.")

# Main loop for the program
def main():
    products = load_products_from_csv()  # Load products from CSV at the start

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
