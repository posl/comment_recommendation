def solve():
    s = input()
    for i in range(1, 10):
        if not str(i) in s:
            print(i)
            return
solve()
