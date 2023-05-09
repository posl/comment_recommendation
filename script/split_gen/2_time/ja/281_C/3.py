def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for a in A:
        sum += a
    r = T % sum
    for i in range(N):
        if r < A[i]:
            print(i+1, r)
            return
        else:
            r -= A[i]
