def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if ans < H[i]:
            ans = H[i]
    print(ans)
