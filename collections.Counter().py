total_shoes = int(input("Enter the total number of shoes- "))
shoe_sizes_input = input("Emter the list of shoe sizes- ").split()
shoe_inventory = []

for size in shoe_sizes_input:
    shoe_inventory.append(int(size))

number_of_customers = int(input("Enter the number of customers- "))
total_earnings = 0

for _ in range(number_of_customers):
    size_requested, price_offered = map(int, input("Give the shoe size and the price- ").split())
    if size_requested in shoe_inventory:
        total_earnings += price_offered
        shoe_inventory.remove(size_requested)

print(total_earnings)
