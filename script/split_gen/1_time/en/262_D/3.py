def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, 1 << N):
        s = 0
        for j in range(N):
            if i >> j & 1:
                s += A[j]
        if s % bin(i).count('1') == 0:
            ans += 1
    print(ans)
