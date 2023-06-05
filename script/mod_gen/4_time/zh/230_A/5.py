def main():
    n = int(input())
    if n <= 21:
        print("AGC0" + str(n-1))
    else:
        print("AGC" + str(n-1))

if __name__ == '__main__':
    main()