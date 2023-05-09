def swap_balls(ball, x):
    if ball == x:
        return x
    elif ball == x-1:
        return x-1
    else:
        return ball

if __name__ == '__main__':
    swap_balls()