def main():
    A,B,C,D = [int(x) for x in input().split()]
    while True:
        C -= B
        if C <= 0:
            print("Yes")
            break
        A -= D
        if A <= 0:
            print("No")
            break

if __name__ == '__main__':
    main()