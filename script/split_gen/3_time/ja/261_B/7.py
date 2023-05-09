def main():
    # input
    n = int(input())
    a = [list(input()) for _ in range(n)]
    # compute
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif a[i][j] == 'W':
                if a[j][i] != 'L':
                    print('incorrect')
                    return
            elif a[i][j] == 'L':
                if a[j][i] != 'W':
                    print('incorrect')
                    return
            elif a[i][j] == 'D':
                if a[j][i] != 'D':
                    print('incorrect')
                    return
    # output
    print('correct')
