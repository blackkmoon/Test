list_of_results = []


def add(a, b):
    return a + b


def subs(a, b):
    return a - b - a


f = {'a': add}

for i, j in zip(range(3), range(3)):
    list_of_results.append(f['a'](i, j))

print(list_of_results)


# what's up
