def main():
    n,k = map(int,input().split())
    if n==0:
        print(0)
    else:
        print(min(n%k,k-n%k))
