def  main():
    n, m = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            d = [10**9] * n
            d[i] = 0
            d[j] = 0
            for _ in range(n):
                for a, b, c in c:
                    if d[a-1] + c < d[b-1]:
                        d[b-1] = d[a-1] + c
            ans += sum(d)
    print(ans)

if __name__ == '__main__':
    ()