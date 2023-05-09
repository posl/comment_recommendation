def check(n, a):
    for i in range(n):
        for j in range(n):
            if i != j:
                if a[i][j] == 'W':
                    if a[j][i] != 'L':
                        return False
                elif a[i][j] == 'L':
                    if a[j][i] != 'W':
                        return False
                elif a[i][j] == 'D':
                    if a[j][i] != 'D':
                        return False
    return True
n = int(input())
a = [list(input()) for _ in range(n)]
print('correct' if check(n, a) else 'incorrect')

if __name__ == '__main__':
    check()