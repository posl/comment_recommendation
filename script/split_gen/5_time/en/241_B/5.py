def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M > N:
        print('No')
    else:
        A.sort()
        B.sort()
        for i in range(M):
            if A[i] > B[i]:
                print('No')
                exit()
        print('Yes')
