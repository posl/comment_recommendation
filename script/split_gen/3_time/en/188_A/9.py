def main():
    # Read the input
    X, Y = map(int, input().split())
    # Write the logic here
    diff = abs(X - Y)
    if diff <= 2:
        print("Yes")
    else:
        print("No")
