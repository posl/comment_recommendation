def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    time = 0
    for i in a:
        time += i
    time = t % time
    if time == 0:
        time = a[n - 1]
    else:
        for i in range(n):
            if time > a[i]:
                time -= a[i]
            else:
                print(i + 1, time)
                break

if __name__ == '__main__':
    main()