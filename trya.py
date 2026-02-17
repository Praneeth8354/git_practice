numbers = []

for i in range(6):
    num = int(input("Enter a number: "))
    numbers.append(num)
print(numbers)
reverse_order = []
for i in range(5,0,-1):
    
    reverse_order.append(numbers[i])
print(reverse_order)