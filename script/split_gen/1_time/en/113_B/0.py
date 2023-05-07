def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans = abs(A - (T - H[i] * 0.006))
        else:
            if ans > abs(A - (T - H[i] * 0.006)):
                ans = abs(A - (T - H[i] * 0.006))
                ans_i = i
    print(ans_i + 1)
