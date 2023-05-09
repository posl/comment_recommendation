def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ''
    while N != 0:
        if N % (-2) != 0:
            ans = '1' + ans
            N -= 1
        else:
            ans = '0' + ans
        N //= (-2)
    print(ans)

if __name__ == '__main__':
    main()