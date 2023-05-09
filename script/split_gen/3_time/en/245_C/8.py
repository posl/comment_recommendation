def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if A[0] > B[-1]:
        A,B = B,A
    if A[-1] + K < B[0]:
        print("No")
        return
    for i in range(N):
        if A[i] + K < B[i]:
            print("No")
            return
    print("Yes")
    return
