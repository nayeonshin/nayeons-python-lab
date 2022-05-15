def count_sort(numbers: list):
    histogram = [0] * 255
    for i in numbers:
        histogram[i] += 1
    cursor = 0
    for i in range(len(histogram)):
        for j in range(histogram[i]):
            numbers[cursor] = i
            cursor += 1
