def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if n < m:
        print("No")
        return
    A.sort()
    B.sort()
    for i in range(m):
        if A[i] >= B[i]:
            print("No")
            return
    print("Yes")
    return
