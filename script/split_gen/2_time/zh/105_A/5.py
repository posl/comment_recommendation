def problem105_a():
    n,k = map(int,input().split())
    print(0 if n%k==0 else 1)
