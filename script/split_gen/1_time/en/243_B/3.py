def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    A_set = set(A)
    B_set = set(B)
    C_set = A_set & B_set
    print(count)
    print(len(C_set) - count)
