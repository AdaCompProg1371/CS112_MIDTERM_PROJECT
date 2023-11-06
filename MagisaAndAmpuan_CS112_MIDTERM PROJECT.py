# Calculation of 7 Grocery Prices
print("Beginning of Program")
print("**************************")

# Type products
product1 = input("Product 1:")
product2 = input("Product 2:")
product3 = input("Product 3:")
product4 = input("Product 4:")
product5 = input("Product 5:")
product6 = input("Product 6:")
product7 = input("Product 7:")
print("**************************")

# Type prices for each product in pesos
price1 = eval(input("Price 1:"))
price2 = eval(input("Price 2:"))
price3 = eval(input("Price 3:"))
price4 = eval(input("Price 4:"))
price5 = eval(input("Price 5:"))
price6 = eval(input("Price 6:"))
price7 = eval(input("Price 7:"))
print("**************************")

# Type number of products for each product provided
quantity1 = int(input("Quantity 1:"))
quantity2 = int(input("Quantity 2:"))
quantity3 = int(input("Quantity 3:"))
quantity4 = int(input("Quantity 4:"))
quantity5 = int(input("Quantity 5:"))
quantity6 = int(input("Quantity 6:"))
quantity7 = int(input("Quantity 7:"))
print("**************************")

# Get valued price or VP for each product in pesos
valued_price1 = price1 * quantity1
print("VP1:" , valued_price1)
valued_price2 = price2 * quantity2
print("VP2:" , valued_price2)
valued_price3 = price3 * quantity3
print("VP3:" , valued_price3)
valued_price4 = price4 * quantity4
print("VP4:" , valued_price4)
valued_price5 = price5 * quantity5
print("VP5:" , valued_price5)
valued_price6 = price6 * quantity6
print("VP6:" , valued_price6)
valued_price7 = price7 * quantity7
print("VP7:" , valued_price7)
print("**************************")

# Compute total price of all seven products in  pesos
total_price = valued_price1 + valued_price2 + valued_price3 + valued_price4 + valued_price5 + valued_price6 + valued_price7
print("Total Price:" , total_price)
print("**************************")

# Insert consumer's age for discount
consumer_age = eval(input("Consumer's Age:"))
if consumer_age < 25:
    discount = "100 pesos"
elif consumer_age == 25:
    discount = "150 pesos"
else:
    discount = "200 pesos"
print("Discount:" , discount)
print("**************************")

# Solve for discounted price in pesos
discounted_price = total_price - consumer_age
discounted_price1 = "{:.2f}".format(discounted_price)
print("Discounted Price:" , discounted_price1)
print("**************************")

# End of program
print("End of Program")