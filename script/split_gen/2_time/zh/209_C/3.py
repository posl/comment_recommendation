def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(0,n,2):
        a[i] -= 1
    if sum(a) <= x:
        print('Yes')
    else:
        print('No')
