def main():
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, 3):
        ans += A[i] - A[i-1]
    print(ans)
