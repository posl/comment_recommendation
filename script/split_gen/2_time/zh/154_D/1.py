def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    ans = sum(p[:k]) + sum(p[-k:])
    print(ans/2)
