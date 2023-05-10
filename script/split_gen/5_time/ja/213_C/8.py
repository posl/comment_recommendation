def main():
    h,w,n = map(int,input().split())
    d = {}
    for i in range(n):
        a,b = map(int,input().split())
        d[(a,b)] = i+1
    a = []
    for i in range(1,h+1):
        a.append([d[(i,j)] for j in range(1,w+1) if (i,j) in d])
    b = []
    for i in range(1,w+1):
        b.append([d[(j,i)] for j in range(1,h+1) if (j,i) in d])
    for i in range(h):
        if len(a[i]) == 0:
            a[i] = [0]
    for i in range(w):
        if len(b[i]) == 0:
            b[i] = [0]
    for i in range(h):
        print(" ".join(map(str,a[i])))
    for i in range(w):
        print(" ".join(map(str,b[i])))
