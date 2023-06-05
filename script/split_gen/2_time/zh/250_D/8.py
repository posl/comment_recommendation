def main():
    n,q = map(int,input().split())
    x = []
    for i in range(q):
        x.append(int(input()))
    #print(x)
    #print(n,q)
    l = [i+1 for i in range(n)]
    #print(l)
    for i in range(q):
        #print('i',i)
        #print('x[i]-1',x[i]-1)
        if x[i] != 1:
            l[x[i]-2],l[x[i]-1] = l[x[i]-1],l[x[i]-2]
            #print(l)
        else:
            l[0],l[1] = l[1],l[0]
            #print(l)
    for i in range(n):
        print(l[i],end=' ')
    print('')
