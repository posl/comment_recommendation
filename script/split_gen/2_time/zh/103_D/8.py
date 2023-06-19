def main():
    n, m = map(int, input().split())
    # print(n, m)
    ab = []
    for i in range(m):
        ab.append(list(map(int, input().split())))
    # print(ab)
    ab.sort(key=lambda x: (x[0], x[1]))
    # print(ab)
    num = 0
    for i in range(m):
        if ab[i][1] <= ab[i+1][0]:
            num += 1
            continue
        else:
            ab[i+1][0] = ab[i][0]
            ab[i+1][1] = min(ab[i][1], ab[i+1][1])
    # print(ab)
    print(num)
