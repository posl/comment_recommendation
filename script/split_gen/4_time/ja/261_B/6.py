def main():
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and a[i][j] == 'W' and a[j][i] != 'L':
                print('incorrect')
                return
            if i != j and a[i][j] == 'L' and a[j][i] != 'W':
                print('incorrect')
                return
            if i != j and a[i][j] == 'D' and a[j][i] != 'D':
                print('incorrect')
                return
    print('correct')
