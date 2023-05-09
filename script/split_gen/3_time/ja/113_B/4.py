def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 10**10
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < min:
            ans = i
            min = abs(T - H[i] * 0.006 - A)
    print(ans + 1)
