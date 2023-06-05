def main():
    n,k = map(int,input().split())
    d = [0]*k
    a = [0]*k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int,input().split()))
    ans = n
    for i in range(k):
        for j in range(d[i]):
            if a[i][j] == ans:
                ans -= 1
    print(ans)
