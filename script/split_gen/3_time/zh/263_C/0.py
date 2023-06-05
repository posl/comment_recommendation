def main():
    n,m = map(int,input().split())
    a = list(range(1,m+1))
    for i in range(1,n):
        a = [x for x in a if x < m-n+i+1]
    print(a)
