import sys
class Supplier:
    def __init__(self,sup_id,sup_name,contact):
        self.sup_id = sup_id
        self.sup_name = sup_name
        self.contact = contact
    def display_supplier(self):
        print("Supplier ID:", self.sup_id)
        print("Supplier Name:", self.sup_name)
        print("Contact:", self.contact)
class Product:
    product_count=0
    class Specification:
        def __init__(self,brand,color,weight):
            self.brand = brand
            self.color = color
            self.weight = weight
        def display_specification(self):
            print("Brand:", self.brand)
            print("Color:", self.color)
            print("Weight:", self.weight,"kg")
    def __init__(self,pro_id,pro_name,price,supplier,brand,colour,weight):
        self.pro_id = pro_id
        self.pro_name = pro_name
        self.price = price
        self.supplier = supplier
        self.spec=Product.Specification(brand,colour,weight)
        Product.product_count+=1
        print(f"\nProduct{self.pro_name}added successfully!")
    def display_product(self):
        print("\n___Product Details__")
        print("Product ID:", self.pro_id)
        print("Product Name:", self.pro_name)
        print("Product Price:", self.price)
        self.spec.display_specification()
        print("\nsupplier details:")
        self.supplier.display_supplier()
        print("Product reference Count:",sys.getrefcount(self.supplier)-1)
    def __del__(self):
        Product.product_count-=1
        print(f"Product{self.pro_name}removed successfully!")
#Main Program
products=[]
while True:
    print("\n__MENU___")
    print("1. Add Product")
    print("2. Display Products")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("\nEnter supplier details")
        sid=int(input("Enter Supplier ID:"))
        sname=input("Enter Supplier Name:")
        contact=int(input("Enter Contact Number:"))
        supplier=Supplier(sid,sname,contact)
        n=int(input("\nHow many products do you want to add?"))
        for i in range(n):
            print(f"\nEnter Product{i+1} details:")
            pid=input("Enter Product ID:")
            pname=input("Enter Product Name:")
            price=float(input("Enter Product Price:"))
            brand=input("Enter Brand Name:")
            colour=input("Enter Brand Colour:")
            weight=int(input("Enter Product Weight:"))
            p=Product(pid,pname,price,supplier,brand,colour,weight)
            products.append(p)
    elif choice==2:
        if products:
            print("\n__Product List__")
            for p in products:
                p.display_product()
            print("\nTotal Products:",Product.product_count)
    elif choice==3:
        print("Exiting Products")
        break
    else:
        print("Invalid Choice")
