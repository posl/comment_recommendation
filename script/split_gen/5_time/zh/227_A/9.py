def main():
    n,k,a = map(int,input().split())
    print((k-(n-a+1))%n+1)
