def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    T = T - A
    ans = 0
    min = 100
    for i in range(N):
        if min > abs(T - H[i] * 0.006):
            min = abs(T - H[i] * 0.006)
            ans = i + 1
    print(ans)
