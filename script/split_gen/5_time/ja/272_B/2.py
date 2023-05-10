def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(m)]
    for i in range(m):
        a[i].pop(0)
    for i in range(m):
        for j in range(i+1,m):
            if len(set(a[i]) & set(a[j])) > 0:
                print("Yes")
                exit()
    print("No")
