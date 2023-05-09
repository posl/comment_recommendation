def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(tuple(map(int, input().split())))
    points_set = set(points)
    points_dict = {}
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                p1 = points[i]
                p2 = points[j]
                if p1[0] == p2[0]:
                    p1, p2 = p2, p1
                if p1[0] < p2[0]:
                    if p1[1] < p2[1]:
                        p3 = (p2[0], p1[1])
                        p4 = (p1[0], p2[1])
                    else:
                        p3 = (p2[0], p2[1])
                        p4 = (p1[0], p1[1])
                else:
                    if p1[1] < p2[1]:
                        p3 = (p1[0], p1[1])
                        p4 = (p2[0], p2[1])
                    else:
                        p3 = (p1[0], p2[1])
                        p4 = (p2[0], p1[1])
                if p3 in points_set and p4 in points_set:
                    if p1 not in points_dict:
                        points_dict[p1] = set()
                    points_dict[p1].add((p3, p4))
    count = 0
    for p1 in points_dict:
        for p2 in points_dict[p1]:
            count += len(points_dict[p1] & points_dict[p2])
    print(count//2)

if __name__ == '__main__':
    main()