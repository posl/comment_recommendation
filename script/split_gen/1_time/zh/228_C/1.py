def main():
    n,k = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    a.sort(key=sum)
    a.reverse()
    b = [sum(a[i][:3]) for i in range(n)]
    b.sort()
    b.reverse()
    for i in range(n):
        if a[i][0] == b[k-1]:
            print('Yes')
        else:
            print('No')
