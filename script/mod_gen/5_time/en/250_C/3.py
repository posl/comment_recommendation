def swap_balls(balls, x):
    for i in range(len(balls)):
        if balls[i] == x:
            if i == len(balls)-1:
                balls[i-1], balls[i] = balls[i], balls[i-1]
            else:
                balls[i], balls[i+1] = balls[i+1], balls[i]
            return balls
    return balls

if __name__ == '__main__':
    swap_balls()