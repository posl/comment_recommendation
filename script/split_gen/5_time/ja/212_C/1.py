def main():
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())))
    #print(a)
    #print(b)
    min_diff = 10**9
    for i in range(n):
        min_diff = min(min_diff,abs(a[i]-b[0]))
        min_diff = min(min_diff,abs(a[i]-b[m-1]))
    for j in range(m):
        min_diff = min(min_diff,abs(a[0]-b[j]))
        min_diff = min(min_diff,abs(a[n-1]-b[j]))
    print(min_diff)
    return
