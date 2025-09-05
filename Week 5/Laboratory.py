# Celsius to Fahrenheit table using while loop
celsius = 10
print(f"{'Celsius':<10}{'Fahrenheit'}")  # Table header

while celsius <= 30:
    fahrenheit = (9/5 * celsius) + 32
    print(f"{celsius:<10}{int(fahrenheit)}")
    celsius += 5


# Count vowels in a phrase using for loop
phrase = input("Enter a phrase: ")
vowels = "aeiouAEIOU"
count = 0

for char in phrase:
    if char in vowels:
        count += 1

print(f"The phrase contains {count} vowels.")
