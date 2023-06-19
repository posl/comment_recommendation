def main():
    n,k,q = map(int,input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    b = [0 for i in range(n)]
    for i in range(q):
        b[a[i]-1]+=1
    for i in range(n):
        if k+ b[i] -q >0:
            print("Yes")
        else:
            print("No")
