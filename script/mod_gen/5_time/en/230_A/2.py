def main():
    n = int(input())
    if n < 10:
        print("AGC00{}".format(n))
    elif n < 100:
        print("AGC0{}".format(n))
    else:
        print("AGC{}".format(n))

if __name__ == '__main__':
    main()