def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    #print(A[-1])
    max_f = 0
    for m in range(0, A[-1]):
        #print(m)
        f = 0
        for i in range(0, N):
            f += m % A[i]
        #print(f)
        if f > max_f:
            max_f = f
    print(max_f)
