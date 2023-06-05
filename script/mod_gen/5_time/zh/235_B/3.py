def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        if i == N - 1:
            ans = H[i]
        elif H[i] < H[i+1]:
            ans = H[i+1]
    print(ans)

if __name__ == '__main__':
    main()