def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    time = 0
    for i in range(n):
        time += a[i]
        if time > t:
            print(i+1, t - time + a[i])
            break
    else:
        print(n, t - time + a[n-1])

if __name__ == '__main__':
    main()