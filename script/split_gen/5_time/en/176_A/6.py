def main():
    N,X,T = map(int, input().split())
    print(int((N+X-1)/X)*T)
