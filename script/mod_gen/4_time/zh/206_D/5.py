def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    cnt = 0
    for i in range(n//2):
        if a[i] != a[i+1]:
            cnt += 1
    print(cnt*2 if n%2==0 else cnt*2+1)

if __name__ == '__main__':
    main()