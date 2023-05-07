def main():
    n = int(input())
    a = list(map(int,input().split()))
    now = 0
    max_x = 0
    for i in range(n):
        now += a[i]
        max_x = max(max_x,now)
    print(max_x)

if __name__ == '__main__':
    main()