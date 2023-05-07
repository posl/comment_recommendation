def solve():
    n = int(input())
    names = set()
    for i in range(n):
        name = input()
        if name in names:
            print("Yes")
            return
        names.add(name)
    print("No")
solve()
