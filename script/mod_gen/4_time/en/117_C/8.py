def main():
    n,m = map(int,input().split())
    x = sorted(map(int,input().split()))
    if n >= m:
        print(0)
        return
    if n == 1:
        print(max(x) - min(x))
        return
    x = sorted([x[i+1] - x[i] for i in range(m-1)])
    print(sum(x[:m-n]))

if __name__ == '__main__':
    main()