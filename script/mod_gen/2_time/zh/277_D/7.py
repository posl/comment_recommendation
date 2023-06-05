def main():
    #n = int(input())
    #ab = [list(map(int, input().split())) for _ in range(n)]
    n = 3
    ab = [[500000000, 600000000], [600000000, 700000000], [700000000, 800000000]]
    ab.sort(key=lambda x: x[1])
    #print(ab)
    ans = 1
    for i in range(n):
        if ans < ab[i][0]:
            ans = ab[i][0]
        if ans >= ab[i][1]:
            ans = ab[i][1]
    print(ans)

if __name__ == '__main__':
    main()