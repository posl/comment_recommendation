def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int, input().split())))
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tlr[i][1] <= tlr[j][1] <= tlr[i][2] or tlr[i][1] <= tlr[j][2] <= tlr[i][2] or tlr[j][1] <= tlr[i][1] <= tlr[j][2] or tlr[j][1] <= tlr[i][2] <= tlr[j][2]:
                count += 1
    print(count)
