def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    total = 0
    for i in range(n):
        total += a[i]/b[i]
    total /= 2
    distance = 0
    for i in range(n):
        if total < a[i]/b[i]:
            distance += total * b[i]
            break
        else:
            distance += a[i]
            total -= a[i]/b[i]
    print(distance)
main()
