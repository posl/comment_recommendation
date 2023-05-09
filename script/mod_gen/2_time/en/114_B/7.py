def main():
    S = input()
    #Initialize the minimum difference to be 753
    min_diff = 753
    #Loop through the string S to find the minimum difference between 753 and the integer X
    for i in range(len(S) - 2):
        #Convert the string to integer
        X = int(S[i : i + 3])
        #Find the difference between 753 and X
        diff = abs(X - 753)
        #If the difference is smaller than the current minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff
    #Print the minimum difference
    print(min_diff)

if __name__ == '__main__':
    main()