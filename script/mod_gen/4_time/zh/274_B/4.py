def problem274_b():
    h, w = map(int, input().split())
    c = []
    for i in range(h):
        c.append(input())
    for j in range(w):
        count = 0
        for i in range(h):
            if c[i][j] == '#':
                count += 1
        print(count, end=' ')
    print()

if __name__ == '__main__':
    problem274_b()