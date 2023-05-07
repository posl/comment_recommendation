def main():
    # Get the input
    A, B, C = [int(x) for x in input().split()]
    # Find the first multiple of C
    # between A and B
    for i in range(A, B + 1):
        if i % C == 0:
            print(i)
            return
    # If there is no multiple of C
    # between A and B
    print(-1)

if __name__ == '__main__':
    main()