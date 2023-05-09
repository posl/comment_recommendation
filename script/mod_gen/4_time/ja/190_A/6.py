def main():
    # input
    A, B, C = map(int, input().split())
    # compute
    if C == 0:
        if A > B:
            result = "Takahashi"
        else:
            result = "Aoki"
    else:
        if B > A:
            result = "Aoki"
        else:
            result = "Takahashi"
    # output
    print(result)

if __name__ == '__main__':
    main()