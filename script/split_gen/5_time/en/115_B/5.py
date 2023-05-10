def solve():
    N = int(input())
    items = [int(input()) for i in range(N)]
    items.sort()
    items[-1] = items[-1] // 2
    print(sum(items))
