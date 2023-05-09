def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    temp = 10**9
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < temp:
            ans = i + 1
            temp = abs(T - H[i] * 0.006 - A)
    print(ans)
