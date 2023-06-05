def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(N-1):
        if H[i] < H[i+1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    print(max(ans, tmp))
