def main():
    N = int(input())
    ans = 0
    for i in range(1, len(str(N))+1):
        ans += (N // (10**i)) * i
        ans += max(0, (N % (10**i) - 10**(i-1) + 1))
    print(ans)

if __name__ == '__main__':
    main()