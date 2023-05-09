def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i-1 for i in a]
    now = 0
    for i in range(61):
        if k & (1<<i):
            now = a[now]
        a = [a[a[j]] for j in range(n)]
    print(now+1)
