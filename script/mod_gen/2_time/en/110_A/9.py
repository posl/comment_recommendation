def main():
    # Read the input
    A, B, C = map(int, input().split())
    # Find the maximum possible amount of the allowance
    max_allowance = 0
    for i in range(1, 3):
        if i == 1:
            allowance = int(str(A) + str(B) + str(C))
        elif i == 2:
            allowance = int(str(A) + str(C) + str(B))
        if allowance > max_allowance:
            max_allowance = allowance
    print(max_allowance)

if __name__ == '__main__':
    main()