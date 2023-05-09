def main():
    n = int(input())
    if n <= 54:
        print("AGC" + str(n + 100)[1:])
    else:
        print("AGC" + str(n + 1000)[1:])

if __name__ == '__main__':
    main()