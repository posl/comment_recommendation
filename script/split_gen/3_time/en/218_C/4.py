def main():
    n = int(input())
    a = [input() for _ in range(n)]
    b = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == '#':
                break
        else:
            continue
        break
    for k in range(n):
        for l in range(n):
            if b[k][l] == '#':
                break
        else:
            continue
        break
    for m in range(n):
        for o in range(n):
            if a[i+m][j+o] != b[k+m][l+o]:
                print('No')
                return
    print('Yes')
