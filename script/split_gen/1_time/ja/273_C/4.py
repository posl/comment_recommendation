def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = sorted(A, reverse=True)
    #print(A)
    for i in range(N):
        if i == 0:
            print(N)
        else:
            if A[i-1] == A[i]:
                continue
            else:
                print(N-i)
