def print_each_with_iter(iterable):
    iterator = iter(iterable)

    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)


def print_each_with_for(iterable):
    for item in iterable:
        print(item)


set_ = {1, 2, 3}
print_each_with_iter(set_)
print_each_with_for(set_)
