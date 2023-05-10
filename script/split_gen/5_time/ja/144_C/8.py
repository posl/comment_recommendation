def solve():
    N = int(input())
    ans = 0
    for i in range(1, 1000000):
        if i * i > N:
            break
        ans = i
    print(ans * 2 - 1)
    return 0
