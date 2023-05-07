def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)
    ans = 0
    for i in range(N, 0, -1):
        if P[i] == 1:
            ans = N - i + 1
            break
    print(ans)

if __name__ == '__main__':
    main()