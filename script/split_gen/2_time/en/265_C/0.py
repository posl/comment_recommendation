def move(position, direction):
    if direction == 'U':
        position[0] -= 1
    elif direction == 'D':
        position[0] += 1
    elif direction == 'L':
        position[1] -= 1
    elif direction == 'R':
        position[1] += 1
    return position
