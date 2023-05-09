def main():
    N = int(input())
    if N == 0:
        print(0)
    else:
        N = -N
        ans = ""
        while N:
            ans = str(N % 2) + ans
            N = (N - N % 2) // (-2)
        print(ans)

if __name__ == '__main__':
    main()