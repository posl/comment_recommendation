def main():
    #input
    N = int(input())
    As = list(map(int, input().split()))
    #compute
    As.sort()
    ans = 0
    for i in range(N):
        if i == 0 or As[i] != As[i-1]:
            ans += 1
    #output
    print(ans)
