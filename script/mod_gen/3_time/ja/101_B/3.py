def main():
    N = int(input())
    S = 0
    while N > 0:
        S += N % 10
        N //= 10
    if S % 3 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()