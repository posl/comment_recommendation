def main():
    # Get input
    num = int(input())
    times = list(map(int, input().split()))
    # Sort the list
    times.sort()
    # Initialize
    oven1 = 0
    oven2 = 0
    # Calculate the time
    for i in range(num):
        if oven1 <= oven2:
            oven1 += times[num-i-1]
        else:
            oven2 += times[num-i-1]
    # Print the result
    if oven1 <= oven2:
        print(oven2)
    else:
        print(oven1)

if __name__ == '__main__':
    main()