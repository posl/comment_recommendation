def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    for i in range(m):
        a.append(a.pop()//2)
    print(sum(a))
main()
