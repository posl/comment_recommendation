def solve():
    s = input()
    a = s.split()
    for i in range(len(a)):
        a[i] = int(a[i])
    if a.count(100) == 1 and a.count(200) == 1 and a.count(300) == 1 and a.count(400) == 1:
        print(1)
    else:
        print(0)
