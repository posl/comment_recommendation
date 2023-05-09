def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()
    i = 0
    for j in range(K):
        while A[i] == B[j]:
            i += 1
            j += 1
        if A[i] > B[j]:
            print('Yes')
            return
    print('No')
