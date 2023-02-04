from collections import Counter

empty_counter = Counter()
a0_counter = Counter()
a0_counter["a"] = 0
a_counter = Counter("a")

print(empty_counter == a0_counter)  # True
print(empty_counter < a0_counter)  # False; they are equal.
print(empty_counter < a_counter)  # True
