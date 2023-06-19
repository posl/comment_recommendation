def main():
    N = int(input())
    if N >= 43:
        print("AGC{:03d}".format(N+1))
    elif N >= 20:
        print("AGC{:03d}".format(N))
    else:
        print("AGC{:03d}".format(N))

if __name__ == '__main__':
    main()