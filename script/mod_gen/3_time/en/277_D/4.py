def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = [0]*(m+1)
    for i in a:
        b[i] = b[i-1] + 1
    print(n - max(b))
main()

if __name__ == '__main__':
    main()