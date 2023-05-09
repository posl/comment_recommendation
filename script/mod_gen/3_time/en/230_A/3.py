def main():
    n = int(input())
    if n < 43:
        print("AGC%03d" % n)
    else:
        print("AGC%03d" % (n + 1))

if __name__ == '__main__':
    main()