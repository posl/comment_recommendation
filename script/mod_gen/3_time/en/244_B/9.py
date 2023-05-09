def move (x, y, dir):
    if dir == 'e':
        return (x + 1, y)
    elif dir == 'w':
        return (x - 1, y)
    elif dir == 'n':
        return (x, y + 1)
    elif dir == 's':
        return (x, y - 1)
    else:
        print('Error: Invalid direction')
        return (x, y)

if __name__ == '__main__':
    move()