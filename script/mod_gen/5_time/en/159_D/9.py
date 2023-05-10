def main():
    # Get the number of balls
    num_balls = int(input())
    # Get the numbers on the balls
    ball_numbers = list(map(int, input().split()))
    # Create a dictionary to store the number of appearances of each ball number
    ball_dict = {}
    for ball_number in ball_numbers:
        if ball_number in ball_dict:
            ball_dict[ball_number] += 1
        else:
            ball_dict[ball_number] = 1
    # Calculate the total number of ways to choose two distinct balls (disregarding order) from the N-1 balls other than the k-th ball so that the integers written on them are equal
    total_ways = 0
    for ball_number in ball_dict:
        total_ways += ball_dict[ball_number] * (ball_dict[ball_number] - 1) // 2
    # Print the number of ways to choose two distinct balls (disregarding order) from the N-1 balls other than the k-th ball so that the integers written on them are equal
    for ball_number in ball_numbers:
        print(total_ways - (ball_dict[ball_number] - 1))

if __name__ == '__main__':
    main()