def isMultipleOf9(N):
    # N is a multiple of 9 if and only if the sum of the digits in the decimal
    # representation of N is a multiple of 9.
    sumOfDigits = 0
    for n in N:
        sumOfDigits += int(n)
    if sumOfDigits % 9 == 0:
        print("Yes")
    else:
        print("No")
