def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if H[i] == 0:
            continue
        ans += 1
        for j in range(i+1, N):
            if H[j] <= H[i]:
                H[j] = 0
            else:
                break
    print(ans)
