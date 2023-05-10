def solve():
    N, M = list(map(int, input().split()))
    k = []
    a = []
    for _ in range(M):
        k.append(int(input()))
        a.append(list(map(int, input().split())))
    print("Yes" if N == 2 * M else "No")
