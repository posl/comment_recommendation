def main():
    n,k = map(int,input().split())
    print((n//k)**3 + (n//k)**2*(n%k) + (n//k)*(n%k)**2 + (n%k)**3)
