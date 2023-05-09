def main():
    N = int(input())
    T = [int(i) for i in input().split()]
    T.sort()
    ans = 0
    for i in range(N-1):
        ans += T[i]
    ans += T[N-1]
    print(ans)

if __name__ == '__main__':
    main()