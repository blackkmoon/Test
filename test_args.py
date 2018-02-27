list_of_results = []


def add(a, b):
    return a + b


f = {'a': add}

for i, j in zip(range(3), range(3)):
    list_of_results.append(f['a'](i, j))

print(list_of_results)



#whast up
