def main():
    n, m = map(int, input().split())
    cakes = []
    for _ in range(n):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(2**3):
        cakes.sort(reverse=True, key=lambda x: (x[0]*((i>>0)&1)*2-1) + (x[1]*((i>>1)&1)*2-1) + (x[2]*((i>>2)&1)*2-1))
        ans = max(ans, sum(map(lambda x: abs(x[0])+abs(x[1])+abs(x[2]), cakes[:m])))
    print(ans)

if __name__ == '__main__':
    main()