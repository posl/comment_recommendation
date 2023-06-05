def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    l = []
    for i in range(m-1):
        l.append(x[i+1] - x[i])
    l.sort()
    print(sum(l[:m-n]))
main()
