def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if N < M:
        print("No")
    else:
        for i in range(M):
            if A[i] < B[i]:
                print("No")
                break
        else:
            print("Yes")
