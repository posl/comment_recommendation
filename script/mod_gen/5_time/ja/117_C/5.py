def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    if n >= m:
        print(0)
    else:
        diff = []
        for i in range(m-1):
            diff.append(x[i+1]-x[i])
        diff.sort()
        print(sum(diff[:m-n]))

if __name__ == '__main__':
    main()