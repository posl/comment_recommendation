def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(N):
        flag = True
        for a, b in AB:
            if a == i + 1 and H[i] <= H[b - 1]:
                flag = False
                break
            if b == i + 1 and H[i] <= H[a - 1]:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
