def main():
    # Get the number of balls and operations
    n, q = map(int, input().split())
    # Get the operations
    x = [int(input()) for _ in range(q)]
    # Create the list of balls
    balls = [i for i in range(1, n + 1)]
    # Loop through the operations
    for i in range(q):
        # Get the index of the ball with the integer x_i written on it
        idx = balls.index(x[i])
        # Swap the ball with the integer x_i written on it with the next ball to the right
        if idx < n - 1:
            balls[idx], balls[idx + 1] = balls[idx + 1], balls[idx]
        # If the ball with the integer x_i written on it was originally the rightmost ball, swap it with the next ball to the left instead
        else:
            balls[idx], balls[idx - 1] = balls[idx - 1], balls[idx]
    # Print the balls
    print(*balls)

if __name__ == '__main__':
    main()