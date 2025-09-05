L = ["sentence", "contains", "five", "words."]
L.insert(0, "This")
print(" ".join(L))

del L[3]
L.insert(3, "six")
L.insert(4, "different")
print(" ".join(L))


# Assume the name entered is: Damith Hearth
name = input("Enter name with two parts: ")
L = name.split()
print("{0:s}, {1:s}".format(L[1], L[0]))


nums = [6, 2, 8, 1]
print("Largest Number:", max(nums))
print("Length:", len(nums))
print("Total:", sum(nums))


tuple1 = ("course", "of", "human", "events", "When", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
print(" ".join(tuple2))