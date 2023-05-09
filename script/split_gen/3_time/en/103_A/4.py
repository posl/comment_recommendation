def main():
    # Get input here
    A_1, A_2, A_3 = map(int, input().strip().split())
    # Calculate result here
    result = 0
    if A_1 == A_2 == A_3:
        result = 0
    elif A_1 == A_2:
        result = abs(A_3 - A_1)
    elif A_1 == A_3:
        result = abs(A_2 - A_1)
    elif A_2 == A_3:
        result = abs(A_1 - A_2)
    else:
        result = min(abs(A_1 - A_2) + abs(A_2 - A_3), abs(A_1 - A_3) + abs(A_3 - A_2), abs(A_2 - A_1) + abs(A_1 - A_3))
    # Print result here
    print(result)
