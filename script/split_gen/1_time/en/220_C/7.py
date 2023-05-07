def solve(N,A,X):
    B = A*100
    sum = 0
    for i in range(1000):
        sum += B[i]
        if sum > X:
            return i+1
N = int(input())
A = list(map(int,input().split()))
X = int(input())
print(solve(N,A,X))
