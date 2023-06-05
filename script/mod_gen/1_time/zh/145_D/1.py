def move(x,y):
    count = 0
    if x == 0 and y == 0:
        return 1
    if x >= 1 and y >= 2:
        count += move(x-1,y-2)
    if x >= 2 and y >= 1:
        count += move(x-2,y-1)
    return count

if __name__ == '__main__':
    move()