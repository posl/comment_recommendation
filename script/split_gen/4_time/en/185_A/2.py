def main():
    # Get input here
    A1, A2, A3, A4 = map(int, input().strip().split())
    # Calculate result here
    result = 0
    if A1 <= 100 and A2 <= 100 and A3 <= 100 and A4 <= 100:
        result = 1
    # Print output here
    print(result)
