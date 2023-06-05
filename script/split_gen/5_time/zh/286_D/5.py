def main():
    N,X = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    #print(A)
    #print(B)
    sum = 0
    for i in range(N):
        sum += A[i]*B[i]
    if sum < X:
        print("No")
    else:
        print("Yes")
