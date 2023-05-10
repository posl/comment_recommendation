def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    pos = 0
    for i in range(N):
        pos += A[i]
        ans = max(ans, pos)
    print(ans)
