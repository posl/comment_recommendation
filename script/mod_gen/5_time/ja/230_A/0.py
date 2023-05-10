def main():
    N = int(input())
    if N < 42:
        print("AGC{:0=3}".format(N))
    else:
        print("AGC{:0=3}".format(N+1))

if __name__ == '__main__':
    main()