def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 0
    for i in range(1,101):
        ans += sum([(X[j]-i)**2 for j in range(N)])
    print(ans)
