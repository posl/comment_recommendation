def main():
    n = int(input())
    xyh = [list(map(int,input().split())) for i in range(n)]
    for i in range(101):
        for j in range(101):
            for k in range(n):
                if xyh[k][2] != 0:
                    H = xyh[k][2] + abs(xyh[k][0]-i) + abs(xyh[k][1]-j)
                    break
            for k in range(n):
                if xyh[k][2] != max(H-abs(xyh[k][0]-i)-abs(xyh[k][1]-j),0):
                    break
            else:
                print(i,j,H)
                return

if __name__ == '__main__':
    main()