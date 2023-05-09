def main():
    # Get input here
    D, T, S = map(int, input().strip().split())
    # Calculate result here
    if D/S <= T:
        result = 'Yes'
    else:
        result = 'No'
    # Print output here
    print(result)
