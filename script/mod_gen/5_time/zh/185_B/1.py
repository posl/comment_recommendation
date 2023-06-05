def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    battery = n
    for i in range(m):
        if i == 0:
            battery -= a[i]
        else:
            battery -= a[i] - b[i - 1]
        if battery <= 0:
            print("No")
            return
        battery += b[i] - a[i]
        battery = min(n, battery)
    battery -= t - b[-1]
    if battery <= 0:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()