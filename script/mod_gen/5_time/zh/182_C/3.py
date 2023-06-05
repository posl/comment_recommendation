def solve():
    N = int(input())
    if N % 3 == 0:
        print(0)
        return
    N = str(N)
    k = len(N)
    for i in range(k):
        for j in range(10):
            if N[i] == str(j):
                continue
            if (int(N) - j) % 3 == 0:
                print(i+1)
                return
    print(-1)
solve()
