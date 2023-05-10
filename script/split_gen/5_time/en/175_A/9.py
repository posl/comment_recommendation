def main():
    # Take input
    s = input()
    # Initialize variables
    max_streak = 0
    streak = 0
    # Compute the streak
    for i in range(3):
        if s[i] == "R":
            streak += 1
        else:
            streak = 0
        if streak > max_streak:
            max_streak = streak
    # Print the result
    print(max_streak)
