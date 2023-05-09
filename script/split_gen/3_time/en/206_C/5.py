def main():
    n = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = n * (n - 1) // 2
    cnt = 1
    for i in range(n - 1):
        if A[i] == A[i + 1]:
            cnt += 1
        else:
            ans -= cnt * (cnt - 1) // 2
            cnt = 1
    ans -= cnt * (cnt - 1) // 2
    print(ans)
