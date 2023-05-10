def main():
    N = int(input())
    if N < 42:
        print("AGC%03d" % N)
    else:
        print("AGC%03d" % (N+1))

if __name__ == '__main__':
    main()