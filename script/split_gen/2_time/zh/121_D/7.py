def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    # print(a)
    # print(b)
    # print(sum(b))
    if sum(b) <= m:
        print(sum([a[i]*b[i] for i in range(n)]))
    else:
        #排序
        # print(sorted(zip(a,b),key=lambda x:x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))
        #排序
        # print(sorted(zip(a,b),key=lambda x:x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0],reverse=True))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True))
        #排序
        # print(sorted(zip(a,b),key=lambda x:x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[1]/x[0]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1]))
        # print(sorted(zip(a,b),key=lambda x:x[0]/x[1],reverse=True
