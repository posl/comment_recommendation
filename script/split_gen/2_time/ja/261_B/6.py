def main():
    n = int(input())
    a = [list(input()) for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                if a[i][j] != '-':
                    print('incorrect')
                    return
            else:
                if a[i][j] == 'W' and a[j][i] != 'L':
                    print('incorrect')
                    return
                elif a[i][j] == 'L' and a[j][i] != 'W':
                    print('incorrect')
                    return
                elif a[i][j] == 'D' and a[j][i] != 'D':
                    print('incorrect')
                    return
    print('correct')
