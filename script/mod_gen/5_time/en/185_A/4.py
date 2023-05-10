def main():
    # Get input here
    A_1, A_2, A_3, A_4 = map(int, input().strip().split())
    # Calculate result here
    result = 0
    if A_1 > 0 and A_2 > 0 and A_3 > 0 and A_4 > 0:
        result = 1
        if A_1 > 1 and A_2 > 1 and A_3 > 1 and A_4 > 1:
            result = 2
            if A_1 > 2 and A_2 > 2 and A_3 > 2 and A_4 > 2:
                result = 3
    # Print result here
    print(result)
main()

if __name__ == '__main__':
    main()