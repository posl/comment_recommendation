def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for x in a:
        d[x] = d.get(x, 0) + 1
    ans = n * (n - 1) // 2
    for x in d.values():
        ans -= x * (x - 1) // 2
    print(ans)
main()
