def main():
    #input
    N = int(input())
    d = list(map(int, input().split()))
    #compute
    d.sort()
    K = d[N//2]
    ans = K - d[N//2-1]
    #output
    print(ans)
