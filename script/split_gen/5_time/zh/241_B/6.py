def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if n<m:
        print("No")
    else:
        count = 0
        for i in range(m):
            for j in range(count,n):
                if A[j] == B[i]:
                    count += 1
                    break
        if count == m:
            print("Yes")
        else:
            print("No")
main()
