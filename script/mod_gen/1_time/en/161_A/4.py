def main():
    #Read input
    X, Y, Z = map(int, input().split())
    #Swap the contents of the boxes A and B
    A = Y
    B = X
    #Swap the contents of the boxes A and C
    C = Z
    #Print the integers contained in the boxes A, B, and C, in this order, with space in between.
    print(A, B, C)

if __name__ == '__main__':
    main()