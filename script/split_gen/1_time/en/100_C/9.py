def main():
    # Take input
    N = int(input())
    a = list(map(int, input().split()))
    # Initialize counter
    counter = 0
    # Loop over the list
    for i in range(N):
        # Check if the element is even
        while a[i] % 2 == 0:
            # Increment counter
            counter += 1
            # Divide by 2
            a[i] /= 2
    # Print the counter
    print(counter)
