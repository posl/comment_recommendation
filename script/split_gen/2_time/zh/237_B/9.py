def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(map(int,input().split())))
    for j in range(w):
        for i in range(h):
            if i == h-1:
                print(a[i][j])
            else:
                print(a[i][j],end=' ')
