def main():
    n, m, t = map(int, input().split())
    battery = n
    last = 0
    for i in range(m):
        a, b = map(int, input().split())
        battery -= (a - last)
        if battery <= 0:
            print("No")
            return
        battery += (b - a)
        if battery > n:
            battery = n
        last = b
    battery -= (t - last)
    if battery <= 0:
        print("No")
    else:
        print("Yes")
main()
