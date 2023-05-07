def main():
    A, B, C, D = [int(x) for x in input().split()]
    while A > 0 and C > 0:
        C -= B
        if C <= 0:
            break
        A -= D
    if A > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()