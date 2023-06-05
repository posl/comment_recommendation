def problem244_b():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in range(n):
        if t[i] == 'S':
            x += 1
        else:
            if x % 2 == 0:
                y += 1
            else:
                y -= 1
    print(x, y)

if __name__ == '__main__':
    problem244_b()