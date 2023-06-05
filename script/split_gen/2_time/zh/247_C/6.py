def solve():
    N = int(input())
    names = []
    for _ in range(N):
        s, t = input().split()
        names.append(s)
        names.append(t)
    if len(set(names)) == 2*N:
        print("Yes")
    else:
        print("No")
