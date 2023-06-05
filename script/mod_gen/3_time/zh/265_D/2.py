def is_ok(a,b,c,d):
    if a < b < c < d:
        return True
    else:
        return False
n,p,q,r = map(int,input().split())
a = list(map(int,input().split()))
a = sorted(a)
for i in range(n-3):
    if is_ok(i,i+1,i+2,i+3):
        if a[i]+a[i+1]+a[i+2] == p and a[i+1]+a[i+2] == q and a[i+2] == r:
            print("Yes")
            exit()
print("No")

if __name__ == '__main__':
    is_ok()