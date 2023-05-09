def main():
    # Read input
    inputList = input().split()
    # Swap the contents of the boxes A and B
    inputList[0], inputList[1] = inputList[1], inputList[0]
    # Swap the contents of the boxes A and C
    inputList[0], inputList[2] = inputList[2], inputList[0]
    # Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(' '.join(inputList))
