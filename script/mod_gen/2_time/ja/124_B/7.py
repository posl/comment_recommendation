def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] >= max(H[:i+1]):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()