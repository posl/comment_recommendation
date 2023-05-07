def main():
    N = int(input())
    if N >= 1 and N <= 9:
        print("AGC00" + str(N))
    elif N >= 10 and N <= 99:
        print("AGC0" + str(N))
    elif N >= 100 and N <= 999:
        print("AGC" + str(N))

if __name__ == '__main__':
    main()