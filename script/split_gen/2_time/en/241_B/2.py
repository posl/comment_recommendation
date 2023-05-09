def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if A[0] < B[0]:
        print('No')
        return
    for i in range(M):
        if A[i] < B[i]:
            print('No')
            return
    print('Yes')
