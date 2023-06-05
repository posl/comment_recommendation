def main():
    n = int(raw_input())
    points = []
    for i in range(n):
        points.append(map(int, raw_input().split()))
    points = sorted(points, key=lambda x: x[1])
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if points[i][0] == points[j][0]:
                continue
            else:
                for k in range(j+1, n):
                    if points[k][1] == points[j][1]:
                        continue
                    else:
                        for l in range(k+1, n):
                            if points[l][0] == points[i][0]:
                                continue
                            else:
                                if points[i][1] == points[k][1] and points[i][0] == points[l][0] and points[j][0] == points[l][0] and points[j][1] == points[k][1]:
                                    count += 1
    print count

if __name__ == '__main__':
    main()