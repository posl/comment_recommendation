def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A + [0]
    ans = 0
    for i in range(1, N+1):
        if A[i] != A[N+1-i]:
            ans += 1
    print(ans)
