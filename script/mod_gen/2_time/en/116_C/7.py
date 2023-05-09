def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if H[i] > H[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()