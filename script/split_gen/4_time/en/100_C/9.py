def main():
    # Get the number of elements in the sequence
    n = int(input())
    # Get the sequence
    a = list(map(int, input().split()))
    # Initialize the number of operations
    op = 0
    # For each element in the sequence
    for i in range(n):
        # Get the current element
        x = a[i]
        # While the current element is divisible by 2
        while x % 2 == 0:
            # Increment the number of operations
            op += 1
            # Divide the current element by 2
            x /= 2
    # Print the number of operations
    print(op)
