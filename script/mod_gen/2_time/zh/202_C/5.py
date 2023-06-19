def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(lambda i: int(i) - 1, input().split()))
    d = [0] * n
    for i in range(n):
        d[c[i]] += 1
    ans = 0
    for i in range(n):
        ans += d[b[i] - 1]
    print(ans)

if __name__ == '__main__':
    main()