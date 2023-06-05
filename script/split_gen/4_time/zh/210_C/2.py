def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    d = {}
    for i in range(n-k+1):
        d[i] = len(set(c[i:i+k]))
    print(max(d.values()))
