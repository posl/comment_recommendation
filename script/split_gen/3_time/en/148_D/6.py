def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    A.sort()
    #print(A)
    count = 0
    for i in range(N):
        if A[i] == i+1:
            count += 1
    if count == N:
        print(0)
    elif count == N-1 and A[0] == 1:
        print(1)
    elif count == N-1 and A[0] != 1:
        print(-1)
    else:
        print(-1)
