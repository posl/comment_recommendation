def main():
    n,k,d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    s = []
    for i in range(n-k+1):
        s.append(sum(a[i:i+k]))
    s.sort(reverse=True)
    for i in s:
        if i%d == 0:
            print(i)
            exit()
    print(-1)
