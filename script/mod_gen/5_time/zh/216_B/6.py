def questionB():
    n = int(input())
    name = []
    for i in range(n):
        name.append(input())
    if len(set(name)) == len(name):
        print("No")
    else:
        print("Yes")
questionB()
