def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(k-1, n):
        print(sorted(p[0:i+1])[-k+1])

if __name__ == '__main__':
    main()