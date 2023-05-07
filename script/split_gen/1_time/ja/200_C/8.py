def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if (A[j] - A[i]) % 200 == 0:
                cnt += 1
            else:
                break
        ans += cnt * (cnt - 1) // 2
    print(ans)
