def main():
    s = []
    for i in range(9):
        s.append(input())
    p = 0
    for i in range(9):
        for j in range(9):
            if s[i][j] == '#':
                p += 1
    print(p)
