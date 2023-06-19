def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    print(n-m)
