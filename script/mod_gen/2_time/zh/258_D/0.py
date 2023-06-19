def main():
    n, x = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort(key=lambda x: x[0]+x[1])
    #print(ab)
    ans = 0
    for i in range(n):
        if x >= ab[i][0]+ab[i][1]:
            ans += ab[i][0]+ab[i][1]
            x -= ab[i][0]+ab[i][1]
        else:
            ans += x
            x = 0
    print(ans)

if __name__ == '__main__':
    main()