def insertion_sort(list_: list) -> None:
    for i in range(1, len(list_)):
        for j in range(i, 0, -1):
            if list_[j - 1] > list_[j]:
                list_[j - 1], list_[j] = list_[j], list_[j - 1]
