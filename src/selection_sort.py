def selection_sort(list_: list) -> None:
    for i in range(len(list_) - 1):
        min_index = i
        for j in range(i + 1, len(list_)):
            if list_[j] < list_[min_index]:
                min_index = j
        list_[i], list_[min_index] = list_[min_index], list_[i]
