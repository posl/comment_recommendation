def main():
    N = int(input())
    T = input()
    x = 0
    y = 0
    for t in T:
        if t == 'S':
            x += 1
        else:
            y += 1
    print(x, y)
