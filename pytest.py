# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food: ")
    if food == "":
        break
    else:
        price = float(input(f"Enter a price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("---------- Shopping cart -----------")

for food in foods:
    print(f"{food}: ${prices[foods.index(food)]:.2f}")

print("---------- YOUR CART ------------")

for price in prices:
    total += price
    
print()
print(f"Total: ${total:.2f}")