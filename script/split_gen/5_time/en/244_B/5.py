def solve():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            y += 1
        else:
            y -= 1
            if t[i] == 'R':
                x *= -1
    print(x, y)
