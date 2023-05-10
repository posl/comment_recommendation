def main():
    # Get input here
    n, a, b = map(int, input().strip().split())
    s = input().strip()
    # Calculate result here
    result = 0
    if a < b:
        result += a * n
    else:
        result += b * n
    # Print output here
    print(result)
