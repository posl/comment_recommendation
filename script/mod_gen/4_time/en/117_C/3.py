def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = []
    for i in range(m-1):
        d.append(x[i+1]-x[i])
    d.sort()
    print(sum(d[:m-n]))

if __name__ == '__main__':
    main()