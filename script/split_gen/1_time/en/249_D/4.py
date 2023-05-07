def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if A[i] % A[j] == 0:
                for k in range(N):
                    if A[j] % A[k] == 0:
                        ans += 1
    print(ans)
