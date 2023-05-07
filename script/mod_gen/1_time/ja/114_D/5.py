def main():
    N = int(input())
    n = N
    i = 2
    d = []
    while i**2 <= n:
        while n%i == 0:
            n //= i
            d.append(i)
        i += 1
    if n > 1:
        d.append(n)
    d.sort()
    print(d)
    cnt = 0
    # 75
    if d.count(5) >= 2 and d.count(3) >= 4:
        cnt += 1
    # 25 * 3
    if d.count(5) >= 1 and d.count(3) >= 2:
        cnt += 1
    # 15 * 5
    if d.count(5) >= 3 and d.count(3) >= 1:
        cnt += 1
    # 5 * 5 * 3
    if d.count(5) >= 4 and d.count(3) >= 1:
        cnt += 1
    # 5 * 5 * 3 * 2
    if d.count(5) >= 4 and d.count(3) >= 2:
        cnt += 1
    # 5 * 5 * 3 * 2 * 2
    if d.count(5) >= 4 and d.count(3) >= 3:
        cnt += 1
    # 5 * 5 * 3 * 2 * 2 * 2
    if d.count(5) >= 4 and d.count(3) >= 4:
        cnt += 1
    # 5 * 5 * 3 * 2 * 2 * 2 * 2
    if d.count(5) >= 4 and d.count(3) >= 5:
        cnt += 1
    # 5 * 5 * 3 * 2 * 2 * 2 * 2 * 2
    if d.count(5) >= 4 and d.count(3) >= 6:
        cnt += 1
    # 5 * 5 * 3 * 2 * 2 * 2 * 2 * 2 * 2
    if d.count(5) >= 4 and d.count(3) >= 7:
        cnt +=

if __name__ == '__main__':
    main()