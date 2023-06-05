def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a = a[::-1]
    cnt = [0]*n
    for i in range(n):
        cnt[i] = k//n
    for i in range(k%n):
        cnt[i] += 1
    for i in range(n):
        print(cnt[a.index(a[i])])

if __name__ == '__main__':
    main()