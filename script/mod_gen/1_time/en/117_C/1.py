def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    diff = [x[i+1] - x[i] for i in range(m-1)]
    diff.sort()
    if m > n:
        print(sum(diff[:m-n]))
    else:
        print(0)

if __name__ == '__main__':
    main()