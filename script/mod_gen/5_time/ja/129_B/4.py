def solve():
    n = int(input())
    ws = list(map(int, input().split()))
    result = 100000000000000
    for i in range(1, n):
        s1 = sum(ws[:i])
        s2 = sum(ws[i:])
        result = min(result, abs(s1 - s2))
    print(result)

if __name__ == '__main__':
    solve()