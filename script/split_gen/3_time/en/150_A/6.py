def main():
    # Read the input
    K, X = map(int, input().split())
    # Check if the coins add up to X yen or more
    if K * 500 >= X:
        print("Yes")
    else:
        print("No")
