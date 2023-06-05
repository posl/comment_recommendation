def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i]/B[i]
        right += A[N-i-1]/B[N-i-1]
    print(left + right)
