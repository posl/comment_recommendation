def main():
    N = int(input())
    i = 1
    while i * i < N:
        i += 1
    if i * i == N:
        print(2 * i - 2)
    elif N <= i * (i - 1) + 1:
        print(2 * i - 3)
    else:
        print(2 * i - 2)
main()

if __name__ == '__main__':
    main()