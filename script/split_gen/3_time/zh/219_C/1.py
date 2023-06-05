def main():
    order = input()
    order = order.lower()
    order = list(order)
    order = sorted(order)
    order = ''.join(order)
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    for i in range(n):
        names[i] = names[i].lower()
    names = sorted(names)
    for i in range(n):
        name = names[i]
        name = list(name)
        for j in range(len(name)):
            name[j] = order.index(name[j])
        names[i] = name
    names = sorted(names)
    for i in range(n):
        name = names[i]
        for j in range(len(name)):
            name[j] = order[name[j]]
        names[i] = name
    for i in range(n):
        print(''.join(names[i]))
