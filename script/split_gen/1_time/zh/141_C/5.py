def main():
    n,k,q = map(int,input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    #print(n,k,q,a)
    b = [k for i in range(n)]
    for i in range(q):
        b[a[i]-1] -= 1
    #print(b)
    for i in range(n):
        if b[i] > 0:
            print("Yes")
        else:
            print("No")
