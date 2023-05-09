def problem235_b():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    max = 0
    for i in range(N):
        if max <= H[i]:
            ans += 1
            max = H[i]
    print(ans)

if __name__ == '__main__':
    problem235_b()