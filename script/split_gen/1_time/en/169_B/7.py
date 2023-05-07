def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    #compute
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10**18:
            ans = -1
            break
    #output
    print(ans)
