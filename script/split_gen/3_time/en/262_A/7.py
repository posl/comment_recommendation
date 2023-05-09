def main():
    # Get input
    Y = int(input())
    # Find next event
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + 2 - (Y % 4))
