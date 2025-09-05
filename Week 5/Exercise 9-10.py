for num in range(1, 10, 2):
    print(num)


total = 0
count = 0

while count < 3:   # loop will run 3 times
    num = int(input("Enter a number: "))
    total = total + num
    count += 1

print("Total:", total)
