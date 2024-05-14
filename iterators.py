my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
try:
    while True:
        print(next(my_iterator))
except StopIteration:
    pass