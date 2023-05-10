def main():
    n,k,d = map(int,input().split())
    a = list(map(int,input().split()))
    s = set()
    for i in range(n-k+1):
        s.add(sum(a[i:i+k]))
    s = [i for i in s if i % d == 0]
    if s:
        print(max(s))
    else:
        print(-1)
