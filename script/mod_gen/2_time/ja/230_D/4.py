def main():
    N, D = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        L, R = LR[i]
        if R - L + 1 >= D:
            ans += 1
            continue
        for j in range(i + 1, N):
            if R + D - 1 >= LR[j][0]:
                R = max(R, LR[j][1])
                if R - L + 1 >= D:
                    ans += 1
                    break
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()