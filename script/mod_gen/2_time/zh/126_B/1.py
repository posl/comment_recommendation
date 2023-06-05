def problems126_a():
    n,k = map(int,input().split())
    s = input()
    print(s[:k-1]+s[k-1].lower()+s[k:])
problems126_a()
