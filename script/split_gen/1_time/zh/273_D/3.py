def get_next_position(x,y,direction):
    if direction == 'L':
        y -= 1
    elif direction == 'R':
        y += 1
    elif direction == 'U':
        x -= 1
    elif direction == 'D':
        x += 1
    return x,y
