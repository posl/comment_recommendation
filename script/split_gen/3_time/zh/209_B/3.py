def main():
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        if (i+1)%2 == 0:
            sum += A[i] - 1
        else:
            sum += A[i]
    if sum <= X:
        print('Yes')
    else:
        print('No')
