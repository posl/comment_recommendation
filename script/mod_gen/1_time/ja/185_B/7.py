def main():
    n, m, t = map(int, input().split())
    time = 0
    battery = n
    for i in range(m):
        a, b = map(int, input().split())
        battery -= a - time
        if battery <= 0:
            print("No")
            return
        battery += b - a
        if battery > n:
            battery = n
        time = b
    battery -= t - time
    if battery <= 0:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()