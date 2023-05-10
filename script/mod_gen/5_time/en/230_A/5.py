def main():
    n = int(input())
    if n <= 21:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n+2))

if __name__ == '__main__':
    main()