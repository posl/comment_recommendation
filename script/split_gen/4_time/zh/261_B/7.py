def main():
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][j] == 'W' and a[j][i] != 'L':
                print('不正确')
                return
            if a[i][j] == 'L' and a[j][i] != 'W':
                print('不正确')
                return
            if a[i][j] == 'D' and a[j][i] != 'D':
                print('不正确')
                return
    print('正确')
