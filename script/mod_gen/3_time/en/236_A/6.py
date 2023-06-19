def swap(s,a,b):
    s=list(s)
    s[a],s[b]=s[b],s[a]
    return "".join(s)
s=input()
a,b=map(int,input().split())
print(swap(s,a-1,b-1))
