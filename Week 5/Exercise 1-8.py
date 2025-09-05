num = 5
while True:
    num = 2 * num
    if num % 4 == 0:
        break
print(num)

num = 3
while num < 15:
    num += 5
print(num)

oceans = ["Atlantic", "Pacific", "Indian", "Arctic", "Antarctic"]
i = len(oceans) - 1
while i >= 0:
    if len(oceans[i]) < 7:
        del oceans[i]
    i = i - 1
print(", ".join(oceans))

for i in range(3, 7):
    print(2 * i)

num = 5
for i in range(num, 2 * num - 2):
    print(i)

for countdown in range(10, 0, -1):
    print(countdown)

numEvens = 0
sumOfEvens = 0

list1 = [2, 9, 6, 7, 12]
for num in list1:
    if num % 2 == 0:
        numEvens += 1
        sumOfEvens += num
print(numEvens, sumOfEvens)

numOfNumbers = 0
list1 = ["three", 4, 5.7, "six", "seven", 8, 3.1416]
for item in list1:
    if isinstance(item, str):
        continue
    numOfNumbers += 1
print(numOfNumbers)

