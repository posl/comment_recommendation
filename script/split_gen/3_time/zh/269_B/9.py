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
            if s[i][j] == "#":
                if a == 0:
                    a = i + 1
                if b == 0:
                    b = i + 1
                if c == 0:
                    c = j + 1
                if d == 0:
                    d = j + 1
                if a > i + 1:
                    a = i + 1
                if b < i + 1:
                    b = i + 1
                if c > j + 1:
                    c = j + 1
                if d < j + 1:
                    d = j + 1
    print(str(a) + " " + str(b))
    print(str(c) + " " + str(d))
