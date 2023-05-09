def main():
    X,Y,N = map(int,input().split())
    ans = 0
    if N >= 3:
        ans += (N//3)*Y
        N = N%3
    if N >= 1:
        ans += X
    print(ans)
