def main():
    n, m = map(int, input().split())
    x = sorted(map(int, input().split()))
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff = sorted(diff, reverse=True)
    print(sum(diff[n-1:]))

if __name__ == '__main__':
    main()