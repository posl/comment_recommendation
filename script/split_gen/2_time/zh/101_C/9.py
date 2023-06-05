def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    if k == 1:
        print(n-1)
    else:
        print((n-2)//(k-1)+1)
