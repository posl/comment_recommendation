def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a//2 for a in A]
    A = list(set(A))
    N = len(A)
    g = A[0]
    for i in range(1, N):
        g = gcd(g, A[i])
    if M < g:
        print(0)
    else:
        print((M//g+1)//2)
