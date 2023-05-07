def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * 2001
    for i in range(N):
        B[A[i]] = 1
    for i in range(2001):
        if B[i] == 0:
            print(i)
            break
