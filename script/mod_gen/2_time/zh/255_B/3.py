def main():
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [list(map(int, input().split())) for _ in range(n)]
    #print(n,k)
    #print(a)
    #print(xy)
    def check(r):
        for i in range(n):
            for j in range(i+1, n):
                if (xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2 > (2*r)**2:
                    return False
        return True
    def solve():
        left = 0
        right = 1000000000
        while right - left > 1e-6:
            mid = (left + right) / 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
    print(solve())

if __name__ == '__main__':
    main()