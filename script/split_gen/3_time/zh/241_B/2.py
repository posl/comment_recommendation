def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    if M > N:
        print('No')
        return
    for i in range(M):
        if B[i] < A[i]:
            print('No')
            return
    print('Yes')
