def main():
    N = int(input())
    if N < 42:
        print("AGC%03d" % N)
    elif N < 54:
        print("AGC%03d" % (N + 1))
    else:
        print("AGC054")

if __name__ == '__main__':
    main()