def main():
    s = [input() for _ in range(10)]
    a, b, c, d = -1, -1, -1, -1
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                if a < 0:
                    a = i
                b = i
                if c < 0:
                    c = j
                d = j
    print(a + 1, b + 1)
    print(c + 1, d + 1)
