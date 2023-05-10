def main():
    n = int(input())
    points = [list(map(int,input().split())) for _ in range(n)]
    points.sort()
    points = list(map(list,zip(*points)))
    x = points[0]
    y = points[1]
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                for k in range(j+1,n):
                    if x[i] == x[k]:
                        if y[i] == y[j] and y[k] == y[i]:
                            ans += 1
                    else:
                        break
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()