def main():
    s = []
    for i in range(10):
        s.append(input())
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                if a == 0:
                    a = i + 1
                else:
                    b = i + 1
                if c == 0:
                    c = j + 1
                else:
                    d = j + 1
    print(a, b)
    print(c, d)
