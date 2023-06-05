def main():
    N = int(input())
    #A, B = [0 for i in range(N)], [0 for i in range(N)]
    #for i in range(N):
    #    A[i], B[i] = map(int, input().split())
    #A.sort()
    #B.sort()
    #print(A)
    #print(B)
    A, B = zip(*[tuple(map(int, input().split())) for i in range(N)])
    A = sorted(A)
    B = sorted(B)
    print(A)
    print(B)
    if N % 2 == 1:
        print(B[N//2] - A[N//2] + 1)
    else:
        print(B[N//2-1] + B[N//2] - A[N//2-1] - A[N//2] + 1)
