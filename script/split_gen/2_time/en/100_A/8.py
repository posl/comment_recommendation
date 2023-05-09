def main():
    # Take input
    a, b = map(int, input().split())
    # Check if the sum is 16 or less
    if a+b <= 16:
        print("Yay!")
    else:
        print(":(")
