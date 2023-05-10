def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    i = 0
    while i < N-2:
        if A[i] == A[i+1]:
            i += 1
            continue
        j = i+1
        while j < N-1:
            if A[j] == A[j+1]:
                j += 1
                continue
            ans += N - (j+1)
            j += 1
        i += 1
    print(ans)
