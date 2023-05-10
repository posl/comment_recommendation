def main():
    N = int(input())
    ans = 0
    while N>1:
        if N%2 == 0:
            N = N//2
        else:
            N = N-1
            ans += 1
    print(ans+1)

if __name__ == '__main__':
    main()