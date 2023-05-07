def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] == 0:
            continue
        ans += 1
        for j in range(i, N):
            if H[j] == 0:
                break
            H[j] -= 1
    print(ans)

if __name__ == '__main__':
    main()