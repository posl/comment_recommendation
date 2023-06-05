def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N%2 == 0:
        a = A[int(N/2)-1] + A[int(N/2)]
        b = B[int(N/2)-1] + B[int(N/2)]
        print(int((b-a)/2+1))
    else:
        a = A[int(N/2)]
        b = B[int(N/2)]
        print(int(b-a+1))
