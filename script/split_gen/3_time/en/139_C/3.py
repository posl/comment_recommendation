def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    for i in range(1,N):
        if H[i-1] >= H[i]:
            ans += 1
        else:
            ans = 0
    print(ans)
main()