def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - i - 1 for i, a in enumerate(A)]
    A.sort()
    b = A[N // 2]
    ans = 0
    for a in A:
        ans += abs(a - b)
    print(ans)
