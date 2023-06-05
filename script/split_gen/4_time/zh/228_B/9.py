def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    a = sorted(a)
    #print(a)
    for i in range(n):
        if a[i] == 0:
            print(n-i-1)
            break
