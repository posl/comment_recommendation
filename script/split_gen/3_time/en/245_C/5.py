def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    X = []
    for i in range(N):
        if abs(A[i]-B[i]) <= K:
            X.append(min(A[i],B[i]))
        else:
            print("No")
            return
    print("Yes")
    return
