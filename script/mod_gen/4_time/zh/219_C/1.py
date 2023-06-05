def sort_by_new_order(x, y):
    for i in range(len(x)):
        if x[i] != y[i]:
            return new_order.index(x[i]) - new_order.index(y[i])
    return len(x) - len(y)
new_order = input()
n = int(input())
names = []
for i in range(n):
    names.append(input())
names.sort(key = lambda x: sort_by_new_order(x, new_order))
for name in names:
    print(name)

if __name__ == '__main__':
    sort_by_new_order()