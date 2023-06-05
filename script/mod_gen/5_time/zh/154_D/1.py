def main():
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    p.sort()
    p = p[-k:]
    print((sum(p)+k)/2)
main()
