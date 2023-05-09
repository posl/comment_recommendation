def check(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                if a[i][j] != '-':
                    return False
            else:
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
a = [input() for i in range(n)]

if __name__ == '__main__':
    check()