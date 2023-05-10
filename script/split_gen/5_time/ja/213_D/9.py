def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    ans = [0] * (2*N-1)
    ans[0] = 1
    ans[1] = A[0]
    ans[2] = 1
    ans[3] = B[0]
    #print(ans)
    for i in range(1,N-1):
        if ans[2*i-1] == A[i]:
            ans[2*i] = B[i]
            ans[2*i+1] = A[i]
        elif ans[2*i-1] == B[i]:
            ans[2*i] = A[i]
            ans[2*i+1] = B[i]
        else:
            print("error")
            exit()
    for i in range(2*N-1):
        print(ans[i], end=" ")
    print()
