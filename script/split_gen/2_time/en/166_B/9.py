def main():
    #input
    n, k = map(int, input().split())
    d = [0] * k
    a = [[] for _ in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    #compute
    ans = 0
    for i in range(1, n+1):
        for j in range(k):
            if i in a[j]:
                ans += 1
                break
    #output
    print(n-ans)
