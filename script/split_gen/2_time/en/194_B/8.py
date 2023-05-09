def main():
    #input
    n = int(input())
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int,input().split())
    
    #compute
    ans = min(max(a[i],b[j]) for i in range(n) for j in range(n) if i!=j)
    
    #output
    print(ans)
