def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*n
    b[0] = 1
    for i in range(1,n):
        for j in a:
            if i-j>=0 and b[i-j]==0:
                b[i] = 1
                break
    for i in range(n-1,-1,-1):
        if b[i]==0:
            print(i)
            break
main()
