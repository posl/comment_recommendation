def main():
    N = int(input())
    H = list(map(int,input().split()))
    m = 0
    ans = 0
    for i in range(N):
        if m < H[i]:
            m = H[i]
            ans = i+1
    print(ans)

if __name__ == '__main__':
    main()