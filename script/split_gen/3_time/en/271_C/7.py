def main():
    #input
    N = int(input())
    a = list(map(int, input().split()))
    #compute
    a.sort()
    ans = 0
    for i in range(N):
        if a[i] <= ans + 1:
            ans += a[i]
        else:
            break
    #output
    print(ans)
