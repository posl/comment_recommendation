def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 10**9
    for i in range(N):
        if abs(T-H[i]*0.006-A) < diff:
            diff = abs(T-H[i]*0.006-A)
            ans = i+1
    print(ans)
