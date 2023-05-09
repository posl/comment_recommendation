def main():
    N, Q = map(int, input().split())
    cars = [i for i in range(N + 1)]
    ans = []
    for i in range(Q):
        c, x, y = map(int, input().split())
        if c == 1:
            cars[x], cars[y] = cars[y], cars[x]
        elif c == 2:
            cars[x], cars[y] = cars[y], cars[x]
        else:
            ans.append(' '.join([str(cars.index(i)) for i in cars if i == x]))
    print('
'.join(ans))

if __name__ == '__main__':
    main()