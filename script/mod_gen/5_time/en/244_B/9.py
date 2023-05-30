def main():
    # Get input here
    N = int(input())
    T = input()
    # Calculate result here
    x = 0
    y = 0
    direction = 0
    for t in T:
        if t == 'S':
            if direction == 0:
                x += 1
            elif direction == 1:
                y -= 1
            elif direction == 2:
                x -= 1
            elif direction == 3:
                y += 1
        elif t == 'R':
            direction += 1
            direction %= 4
    # Print output here
    print(x, y)
main()
