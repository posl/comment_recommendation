def main():
    A,B,N = map(int,input().split())
    if B<=N:
        x=B-1
    else:
        x=N
    print(int((A*x)/B)-A*int(x/B))
