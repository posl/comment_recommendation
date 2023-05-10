def solve():
    n = int(input())
    points = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                x3,y3 = points[k]
                if (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2):
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    solve()