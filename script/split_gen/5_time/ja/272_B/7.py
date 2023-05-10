def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(m)]
    b = []
    for i in range(m):
        for j in range(1,a[i][0]+1):
            b.append(a[i][j])
    c = list(set(b))
    if len(c) == len(b):
        print('No')
    else:
        print('Yes')
