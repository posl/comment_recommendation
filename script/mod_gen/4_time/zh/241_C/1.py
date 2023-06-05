def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        s[i] = s[i].replace('#', '1')
        s[i] = s[i].replace('.', '0')
    for i in range(n):
        s[i] = int(s[i], 2)
    for i in range(n):
        s[i] = bin(s[i])
    for i in range(n):
        s[i] = s[i].replace('0b', '')
        s[i] = s[i].rjust(n, '0')
    for i in range(n):
        s[i] = list(s[i])
        for j in range(n):
            s[i][j] = int(s[i][j])
    for i in range(n):
        for j in range(n):
            if s[i][j] == 1:
                for k in range(1, 6):
                    if i+k < n and s[i+k][j] == 1:
                        for l in range(1, 6):
                            if j+l < n and s[i][j+l] == 1:
                                if i+k+l < n and s[i+k+l][j+l] == 1:
                                    print('Yes')
                                    exit()
    print('No')
main()
