def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if M > N:
        print("No")
    else:
        A.sort()
        B.sort()
        i = 0
        j = 0
        while i < M and j < N:
            if B[i] <= A[j]:
                i += 1
            j += 1
        if i == M:
            print("Yes")
        else:
            print("No")
