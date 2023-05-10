def main():
    n = int(input())
    if n < 42:
        print("AGC{:03d}".format(n))
    else:
        print("AGC{:03d}".format(n+1))

if __name__ == '__main__':
    main()