def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for a in A:
        B[a] += 1
    ans = 0
    for b in B:
        ans += b * (b - 1) // 2
    for a in A:
        print(ans - B[a] + 1)
