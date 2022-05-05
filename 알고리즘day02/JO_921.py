n = int(input())

#squared_numbers = []
#for i in range(1, n + 1):
#    squared_numbers.append(i ** 2)

# List comprehension
squared_numbers=[i ** 2 for i in range(1, n + 1)]

print(squared_numbers)