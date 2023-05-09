def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    Bc = [0] * (n + 1)
    for c in C:
        Bc[c] += 1
    Bcsum = [0] * (n + 1)
    for i in range(1, n + 1):
        Bcsum[i] = Bcsum[i - 1] + Bc[i]
    ans = 0
    for a in A:
        ans += Bcsum[B[a - 1]]
    print(ans)
