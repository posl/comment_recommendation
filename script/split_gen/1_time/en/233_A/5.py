def main():
    # Read in input
    X, Y = map(int, input().split())
    # Calculate the minimum number of 10-yen stamps to add
    stamps = (Y - (X % Y)) % Y
    # Print the answer
    print(stamps)
