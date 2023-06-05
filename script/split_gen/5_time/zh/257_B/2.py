def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    s = []
    for i in range(n):
        s.append(0)
    for i in range(k):
        s[a[i]-1] += 1
    for i in range(q):
        for j in range(k):
            if s[l[j]-1] == 1 and l[j] != n:
                s[l[j]-1] -= 1
                s[l[j]] += 1
            elif s[l[j]-1] == 1 and l[j] == n:
                s[l[j]-1] -= 1
            else:
                continue
    for i in range(n):
        if s[i] == 1:
            print(i+1,end=' ')
        else:
            continue
