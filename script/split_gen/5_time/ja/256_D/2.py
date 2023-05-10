def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    l.sort()
    minl = l[0][0]
    maxr = l[0][1]
    for i in range(1,n):
        if l[i][0] <= maxr:
            maxr = max(maxr,l[i][1])
        else:
            print(minl,maxr)
            minl = l[i][0]
            maxr = l[i][1]
    print(minl,maxr)
