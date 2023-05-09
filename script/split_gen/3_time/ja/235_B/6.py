def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += H[i]
        elif H[i-1] < H[i]:
            ans += H[i] - H[i-1]
    print(ans)
