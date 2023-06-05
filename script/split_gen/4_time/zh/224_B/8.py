def f(h,w,a):
    for i in range(h):
        for j in range(w):
            for ii in range(i+1,h):
                for jj in range(j+1,w):
                    if (a[i][j]+a[ii][jj])>(a[ii][j]+a[i][jj]):
                        return 'No'
    return 'Yes'
h,w=map(int,input().split())
a=[]
for i in range(h):
    a.append(list(map(int,input().split())))
print(f(h,w,a))
