def main():
    N = int(input())
    if N == 0:
        print(0)
        exit()
    ans = ""
    while N != 0:
        if N % -2 == 0:
            ans = "0" + ans
        else:
            ans = "1" + ans
        N = (N - N % -2) // -2
    print(ans)

if __name__ == '__main__':
    main()