def main():
    A = list(map(int, input().split()))
    ans = 0
    for i in range(len(A)):
        ans += A[i] // 100
        ans += A[i] % 100
    print(ans // 100)
