def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        ans = str(N & 1) + ans
        N = -(N >> 1)
    print(ans)

if __name__ == '__main__':
    main()