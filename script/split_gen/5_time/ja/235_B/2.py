def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        if H[i] < H[i+1]:
            ans = 0
        else:
            ans += 1
    print(ans)