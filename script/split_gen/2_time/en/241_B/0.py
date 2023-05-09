def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    j = 0
    for i in range(M):
        while j < N and A[j] < B[i]:
            j += 1
        if j == N or A[j] > B[i]:
            print("No")
            return
        j += 1
    print("Yes")
