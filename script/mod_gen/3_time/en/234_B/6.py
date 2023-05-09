def main():
    import math
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, math.sqrt((xy[i][0]-xy[j][0])**2+(xy[i][1]-xy[j][1])**2))
    print(ans)
    return
main()

if __name__ == '__main__':
    main()