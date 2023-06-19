def main():
    n,k = map(int,input().split())
    p = [list(map(int,input().split())) for _ in range(n)]
    print(p)
    for i in range(n):
        if p[i][0]+p[i][1]+p[i][2] >= k:
            print('Yes')
        else:
            print('No')
