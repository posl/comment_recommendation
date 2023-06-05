def main():
    s = []
    for i in range(10):
        s.append(input())
    print(s)
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                print(i, j)
