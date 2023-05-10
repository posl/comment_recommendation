def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    koma = [0] * n
    for i in range(k):
        koma[a[i]-1] += 1
    for i in range(q):
        koma[l[i]-1] += 1
    for i in range(n):
        if koma[i] > 0:
            print("Yes")
        else:
            print("No")
