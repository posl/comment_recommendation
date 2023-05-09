def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    ans = 0
    for i in range(1,N):
        ans += (X[i]-X[i-1])*(N-i)*i
    print(ans)
