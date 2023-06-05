def main():
    N = int(input())
    if N < 10:
        print("AGC00", N, sep="")
    elif N < 100:
        print("AGC0", N, sep="")
    else:
        print("AGC", N, sep="")

if __name__ == '__main__':
    main()