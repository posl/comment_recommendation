def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    dir = 0
    for i in range(N):
        if T[i] == 'S':
            if dir == 0:
                x += 1
            elif dir == 1:
                y -= 1
            elif dir == 2:
                x -= 1
            elif dir == 3:
                y += 1
        elif T[i] == 'R':
            dir = (dir + 1) % 4
    print(x, y)
