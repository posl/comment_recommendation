def main():
    # Get the input
    rating = int(input())
    # Check the conditions
    if rating < 1200:
        print("ABC")
    elif rating < 2800:
        print("ARC")
    else:
        print("AGC")
