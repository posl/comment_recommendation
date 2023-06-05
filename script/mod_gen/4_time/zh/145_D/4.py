def move(x,y):
    if x==0 and y==0:
        return 1
    elif x<0 or y<0:
        return 0
    else:
        return move(x-1,y-2)+move(x-2,y-1)

if __name__ == '__main__':
    move()