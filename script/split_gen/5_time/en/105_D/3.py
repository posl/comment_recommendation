def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
    A = [a % M for a in A]
    A.sort()
    A.append(1)
    ans = 0
    now = 0
    cnt = 0
    for a in A:
        if a == now:
            cnt += 1
        else:
            ans += cnt * (cnt-1) // 2
            now = a
            cnt = 1
    print(ans)
