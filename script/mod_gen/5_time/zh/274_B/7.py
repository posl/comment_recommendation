def problems274_b():
    h,w = input().split()
    h = int(h)
    w = int(w)
    l = []
    for i in range(h):
        l.append(input())
    for j in range(w):
        count = 0
        for i in range(h):
            if l[i][j] == '#':
                count = count + 1
        print(count,end=' ')
    print()

if __name__ == '__main__':
    problems274_b()