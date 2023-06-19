def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    #print(n,k,p)
    #print(p[:k])
    for i in range(k-1,n):
        print(sorted(p[:i+1],reverse=True)[k-1])
