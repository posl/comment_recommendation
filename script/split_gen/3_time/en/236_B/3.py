def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(2*N):
        if A[2*i] != A[2*i+1]:
            print(A[2*i])
            return
main()
