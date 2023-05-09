def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    direction = 'E'
    for i in range(N):
        if T[i] == 'S':
            if direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
            elif direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
        if T[i] == 'R':
            if direction == 'E':
                direction = 'S'
            elif direction == 'S':
                direction = 'W'
            elif direction == 'W':
                direction = 'N'
            elif direction == 'N':
                direction = 'E'
    print(x,y)
