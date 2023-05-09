def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        a = A[i]
        while a % 2 == 0:
            a = a // 2
            ans += 1
    print(ans)
