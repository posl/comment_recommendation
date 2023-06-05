def main():
    n,m,q = map(int,input().split())
    l = [0 for i in range(m)]
    r = [0 for i in range(m)]
    p = [0 for i in range(q)]
    q = [0 for i in range(q)]
    for i in range(m):
        l[i],r[i] = map(int,input().split())
    for i in range(q):
        p[i],q[i] = map(int,input().split())
    for i in range(q):
        count = 0
        for j in range(m):
            if p[i]<=l[j] and r[j]<=q[i]:
                count += 1
        print(count)
