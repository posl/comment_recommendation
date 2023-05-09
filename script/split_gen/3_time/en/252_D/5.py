def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-2):
        if A[i] == A[i+1]:
            continue
        for j in range(i+1, N-1):
            if A[j] == A[j+1]:
                continue
            for k in range(j+1, N):
                if A[k] == A[k-1]:
                    continue
                if A[i] + A[j] > A[k]:
                    ans += 1
                else:
                    break
    print(ans)
