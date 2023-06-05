def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
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
a = []
for i in range(n):
    a.append(list(input()))

if __name__ == '__main__':
    check()