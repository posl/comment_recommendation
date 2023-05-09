def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    C.append(0)
    ans = 1
    for i in range(N):
        ans *= (C[i] - i)
        ans %= 1000000007
    print(ans)
    return

if __name__ == '__main__':
    main()