def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    points.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0]:
                continue
            for k in range(j+1, n):
                if points[i][1] == points[k][1]:
                    continue
                if points[i][0] == points[k][0]:
                    continue
                for l in range(k+1, n):
                    if points[i][1] == points[l][1]:
                        continue
                    if points[j][1] == points[l][1]:
                        continue
                    if points[k][0] == points[l][0]:
                        continue
                    if points[k][1] == points[l][1]:
                        continue
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()