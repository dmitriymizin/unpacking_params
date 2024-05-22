def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, )
print_params(2, 3)
print_params('str', 5, False)


def print_params2(a, b):
    print(a, b)
values_list_2 = [2, 'str']

print_params2(*values_list_2)


