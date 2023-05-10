def main():
    N = int(input())
    count = 0
    if N == 1:
        print(1)
    else:
        while N > 0:
            if N >= 729:
                N = N - 729
                count += 1
            elif N >= 81:
                N = N - 81
                count += 1
            elif N >= 9:
                N = N - 9
                count += 1
            elif N >= 36:
                N = N - 36
                count += 1
            elif N >= 6:
                N = N - 6
                count += 1
            elif N >= 1:
                N = N - 1
                count += 1
        print(count)

if __name__ == '__main__':
    main()