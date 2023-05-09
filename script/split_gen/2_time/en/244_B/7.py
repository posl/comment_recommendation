def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    face = 0
    for t in T:
        if t == 'S':
            if face == 0:
                x += 1
            elif face == 1:
                y -= 1
            elif face == 2:
                x -= 1
            elif face == 3:
                y += 1
        elif t == 'R':
            face = (face + 1) % 4
    print(x, y)
