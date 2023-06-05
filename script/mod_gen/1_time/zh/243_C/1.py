def isCollision():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    s = input()
    # print(n, x, y, s)
    # print(x[0], y[0])
    # print(x[1], y[1])
    # print(x[2], y[2])
    # print(s)
    for i in range(n):
        if s[i] == 'R':
            x[i] += 1
        elif s[i] == 'L':
            x[i] -= 1
    # print(x)
    for i in range(n):
        for j in range(i+1, n):
            if x[i] == x[j] and y[i] == y[j]:
                return 'Yes'
    return 'No'

if __name__ == '__main__':
    isCollision()