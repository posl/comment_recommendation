def main():
    # Read input
    K, X = map(int, input().split())
    # Calculate
    if 500 * K >= X:
        print("Yes")
    else:
        print("No")
