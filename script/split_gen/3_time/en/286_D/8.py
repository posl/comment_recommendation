def main():
    N,X = map(int,input().split())
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    for i in range(2**N):
        temp = 0
        for j in range(N):
            if (i>>j)&1:
                temp += A[j]*B[j]
        if temp == X:
            print("Yes")
            return
    print("No")
