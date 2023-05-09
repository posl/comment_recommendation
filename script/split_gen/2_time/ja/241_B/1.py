def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    for i in range(M):
        if i == 0:
            if A[i] > B[i]:
                print("No")
                return
        else:
            if A[i] > B[i] or A[i-1] == A[i]:
                print("No")
                return
    print("Yes")
main()
