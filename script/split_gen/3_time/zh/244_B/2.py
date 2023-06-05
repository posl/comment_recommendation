def main():
    # input
    n = int(input())
    t = input()
    # init
    x = 0
    y = 0
    # loop
    for i in range(n):
        if t[i] == 'S':
            if y == 0:
                x += 1
            elif y > 0:
                y -= 1
            elif y < 0:
                y += 1
        elif t[i] == 'R':
            if y == 0:
                y -= x
                x = 0
            elif y > 0:
                x += y
                y = 0
            elif y < 0:
                x -= y
                y = 0
    # output
    print(x, y)
    return
