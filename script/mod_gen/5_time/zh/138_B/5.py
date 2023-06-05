def solve():
    n = int(input())
    a = list(map(int, input().split()))
    sum = 0
    for i in a:
        sum += 1/i
    print(1/sum)
solve()
