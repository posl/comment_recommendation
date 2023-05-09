def main():
    N = int(input())
    z = 2
    count = 0
    while N > 1:
        if N % z == 0:
            count += 1
            N = N // z
        else:
            z += 1
    print(count)

if __name__ == '__main__':
    main()