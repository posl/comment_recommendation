def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        print('No')
    else:
        A.sort()
        B.sort()
        for i in range(N - M + 1):
            if A[i:i + M] == B:
                print('Yes')
                break
        else:
            print('No')
