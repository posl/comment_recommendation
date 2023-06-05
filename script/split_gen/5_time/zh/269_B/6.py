def main():
    s = []
    for i in range(10):
        s.append(list(input()))
    for i in range(10):
        for j in range(10):
            if s[i][j] == '#':
                print(i + 1, j + 1)
                return
