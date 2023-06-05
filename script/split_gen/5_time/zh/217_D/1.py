def main():
    l,q = map(int,input().split())
    mark = [0] * (l+1)
    mark[1] = l
    for i in range(q):
        c,x = map(int,input().split())
        if c == 1:
            mark[x],mark[x+1] = x,mark[x]-x
        else:
            print(mark[x])
