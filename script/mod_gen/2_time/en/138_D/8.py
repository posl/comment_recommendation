def main():
    # Write your code here
    n,q=map(int,input().split())
    p=[0]*n
    for i in range(n-1):
        a,b=map(int,input().split())
        p[b-1]=a-1
    x=[0]*n
    for i in range(q):
        p_,x_=map(int,input().split())
        x[p_]+=x_
    for i in range(n-1,0,-1):
        x[p[i]]+=x[i]
    print(*x)
main()

if __name__ == '__main__':
    main()