def main():
    N = int(input())
    T,A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 1000000
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < min:
            min = abs(A - (T - H[i] * 0.006))
            ans = i + 1
    print(ans)
