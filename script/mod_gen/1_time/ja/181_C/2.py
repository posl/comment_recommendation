def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if (y2-y1)*(x3-x2) == (y3-y2)*(x2-x1):
                    print('Yes')
                    return
    print('No')
main()

if __name__ == '__main__':
    main()