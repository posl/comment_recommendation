def main():
    n = int(input())
    a = []
    x = []
    y = []
    for i in range(n):
        a.append(int(input()))
        temp_x = []
        temp_y = []
        for j in range(a[i]):
            temp = input().split()
            temp_x.append(int(temp[0]))
            temp_y.append(int(temp[1]))
        x.append(temp_x)
        y.append(temp_y)
    ans = 0
    for i in range(2 ** n):
        honest = []
        flag = True
        for j in range(n):
            if (i >> j) & 1:
                honest.append(j)
        for j in range(len(honest)):
            for k in range(a[honest[j]]):
                if ((i >> (x[honest[j]][k] - 1)) & 1) ^ y[honest[j]][k]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            ans = max(ans, len(honest))
    print(ans)
