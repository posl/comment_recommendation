def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        s = 0
        c = 0
        for j in range(N):
            if (i >> j) & 1:
                s += A[j]
                c += 1
        if s % c == 0:
            ans += 1
    print(ans)
