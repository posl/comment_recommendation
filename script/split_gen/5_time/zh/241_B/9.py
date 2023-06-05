def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if n < m:
        print("No")
    else:
        for i in range(m):
            if A[i] < B[i]:
                print("No")
                break
            else:
                if i == m-1:
                    print("Yes")
