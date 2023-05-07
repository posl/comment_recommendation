def main():
    # Get input here
    a, b = map(int, input().strip().split())
    # Calculate result here
    result = 0
    for i in range(a, b+1):
        result += 1
    # Print output here
    print(result)
