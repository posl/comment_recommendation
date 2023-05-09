def main():
    n = int(input())
    v = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]
    print(ans)
main()
