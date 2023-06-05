def main():
    N,K=map(int,input().split())
    p=list(map(int,input().split()))
    p.sort()
    result=0
    for i in range(K):
        result+=p[i]
    print(result)
