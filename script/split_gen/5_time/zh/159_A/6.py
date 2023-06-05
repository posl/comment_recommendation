def main():
    n,m = map(int, input().split())
    print((n*(n-1)+m*(m-1))//2)
