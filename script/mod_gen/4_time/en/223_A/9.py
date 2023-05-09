def problem223_a():
    # Store the input
    x = int(input())
    # Check if the value is between 0 and 1000
    if 0 <= x <= 1000:
        # Check if the value is divisible by 100
        if x % 100 == 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    problem223_a()