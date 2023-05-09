def find_vertex(n,x,s):
    v=[x]
    for i in range(n):
        if s[i]=='U':
            v.append(v[i]//2)
        elif s[i]=='L':
            v.append(v[i]*2)
        else:
            v.append(v[i]*2+1)
    return v[n]
n,x=map(int,input().split())
s=input()
print(find_vertex(n,x,s))
