def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = sorted(A)
    ans = 0
    i = 0
    j = N-1
    while i < j:
        if A[i] == A[j]:
            i += 1
            j -= 1
        else:
            ans += 1
            if A[i] < A[j]:
                i += 1
                A[i] += A[i-1]
            else:
                j -= 1
                A[j] += A[j+1]
    print(ans)
