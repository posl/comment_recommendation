def main():
    n,k,q = map(int,input().split())
    A = [0]*n
    for i in range(q):
        a = int(input())
        A[a-1] += 1
    for i in range(n):
        if k+ A[i] - q > 0:
            print("Yes")
        else:
            print("No")
main()
