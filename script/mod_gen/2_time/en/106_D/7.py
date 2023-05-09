def main():
    n, m, q = [int(x) for x in input().split()]
    trains = [0] * (n + 1)
    for i in range(m):
        l, r = [int(x) for x in input().split()]
        trains[l - 1] += 1
        trains[r] -= 1
    for i in range(n):
        trains[i + 1] += trains[i]
    for i in range(q):
        p, q = [int(x) for x in input().split()]
        print(trains[q] - trains[p - 1])

if __name__ == '__main__':
    main()