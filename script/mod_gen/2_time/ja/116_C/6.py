def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            if h[i] > h[j]:
                break
        else:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()