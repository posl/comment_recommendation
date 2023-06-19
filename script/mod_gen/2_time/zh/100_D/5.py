def main():
    n,m = map(int, input().split())
    cakes = []
    for i in range(n):
        cakes.append(list(map(int, input().split())))
    cakes.sort(key=lambda x: x[0]+x[1]+x[2], reverse=True)
    ans = 0
    for i in range(m):
        ans += cakes[i][0]+cakes[i][1]+cakes[i][2]
    print(ans)

if __name__ == '__main__':
    main()