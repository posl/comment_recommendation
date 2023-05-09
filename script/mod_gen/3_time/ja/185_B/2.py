def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        tmp_a, tmp_b = map(int, input().split())
        a.append(tmp_a)
        b.append(tmp_b)
    battery = n
    for i in range(m):
        if i == 0:
            battery -= a[i]
        else:
            battery -= a[i] - b[i-1]
        if battery <= 0:
            print("No")
            return
        battery += b[i] - a[i]
        if battery > n:
            battery = n
    battery -= t - b[-1]
    if battery <= 0:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()