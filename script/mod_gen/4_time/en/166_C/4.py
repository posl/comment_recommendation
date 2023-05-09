def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(1, N+1):
        flag = True
        for a, b in AB:
            if i == a:
                if H[i-1] <= H[b-1]:
                    flag = False
                    break
            elif i == b:
                if H[i-1] <= H[a-1]:
                    flag = False
                    break
        if flag:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()