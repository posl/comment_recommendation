def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if (x1-x2)*(y2-y3) == (x2-x3)*(y1-y2):
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()