def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda x: int(x) - 1, input().split()))
    d = [0 for _ in range(n)]
    for i in range(n):
        d[b[c[i]]] += 1
    ans = 0
    for i in range(n):
        ans += d[a[i]]
    print(ans)

if __name__ == '__main__':
    main()