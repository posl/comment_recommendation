def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N == 1:
        if abs(A[0]-B[0]) <= K:
            print("Yes")
        else:
            print("No")
        return
    if A[0] == B[0]:
        if abs(A[1]-B[1]) <= K:
            print("Yes")
        else:
            print("No")
        return
    if abs(A[0]-B[0]) <= K:
        print("Yes")
        return
    if abs(A[0]-B[0]) > K:
        print("No")
        return

if __name__ == '__main__':
    main()