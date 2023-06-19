def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    x = []
    for i in range(q):
        x.append(int(input()))
    #print(n,q,a,x)
    print(solve(n,q,a,x))
