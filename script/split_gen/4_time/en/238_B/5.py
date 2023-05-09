def main():
    n = int(input())
    a = list(map(int,input().split()))
    s = 180*(n+1)
    for i in range(n):
        s -= a[i]
    print(s)
