def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = []
    for i in range(N):
        B_C.append(B[C[i]-1])
    B_C.sort()
    A.sort()
    count = 0
    for i in range(N):
        if A[i] == B_C[i]:
            count += 1
    print(count)
