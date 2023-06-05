def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    min_num = A[0]
    start = 0
    end = 0
    for i in range(N):
        if min_num > A[i]:
            min_num = A[i]
            start = i
        if min_num == 1:
            end = i
            break
    if end < start + K - 1:
        print(1)
    else:
        print((end - start) // (K - 1) + 1)
