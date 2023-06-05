def main():
    n,k,a = map(int,input().split())
    if (n-a+1) >= k:
        print(a+k-1)
    else:
        print(k-(n-a+1) % n)
