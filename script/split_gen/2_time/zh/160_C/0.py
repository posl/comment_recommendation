def main():
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    a.append(k)
    b = [0]
    for i in range(n):
        b.append(a[i+1]-a[i])
    b.sort()
    print(sum(b[0:n-1]))
main()
