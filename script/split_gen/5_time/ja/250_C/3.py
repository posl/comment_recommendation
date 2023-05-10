def main():
    n,q = map(int,input().split())
    x = [i for i in range(n)]
    for i in range(q):
        a = int(input())
        x[a-1],x[a] = x[a],x[a-1]
    for i in range(n):
        print(x[i]+1,end=" ")
    print()
