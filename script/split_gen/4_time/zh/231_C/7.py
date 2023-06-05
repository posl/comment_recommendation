def main():
    n,q=map(int,input().split())
    A=list(map(int,input().split()))
    x=[int(input()) for _ in range(q)]
    A.sort()
    for i in range(q):
        print(n - len([a for a in A if a < x[i]]))
