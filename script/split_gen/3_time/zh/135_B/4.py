def solve():
    N = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(N - 1):
        if p[i] == i + 1:
            count += 1
    if count == N - 1:
        print("YES")
    else:
        print("NO")
