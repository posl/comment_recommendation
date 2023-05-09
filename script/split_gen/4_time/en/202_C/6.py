def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [B[C[i]-1] for i in range(N)]
    A.sort()
    B.sort()
    count = 0
    i = 0
    j = 0
    while i < N and j < N:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            count += 1
            i += 1
            j += 1
    print(count)
