def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    flag = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif a[i][j] == 'W':
                if a[j][i] != 'L':
                    flag = 1
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    flag = 1
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    flag = 1
    if flag == 1:
        print('不正确')
    else:
        print('正确')
