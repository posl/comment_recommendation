def main():
    n = int(input())
    a = list(map(int, input().split()))
    sub = [0 for i in range(n)]
    for i in range(n-1):
        sub[a[i]-1] += 1
    for i in range(n):
        print(sub[i])

if __name__ == '__main__':
    main()