def solve():
    n, k = map(int, input().split())
    s = input()
    result = 0
    for i in range(n):
        if s[i] == "0":
            result += 1
    result += min(k, n - 1)
    print(result)

if __name__ == '__main__':
    solve()