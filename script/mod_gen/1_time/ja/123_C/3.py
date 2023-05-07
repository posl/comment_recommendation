def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    if N % A == 0:
        train = int(N / A)
    else:
        train = int(N / A) + 1
    if N % B == 0:
        bus = int(N / B)
    else:
        bus = int(N / B) + 1
    if N % C == 0:
        taxi = int(N / C)
    else:
        taxi = int(N / C) + 1
    if N % D == 0:
        plane = int(N / D)
    else:
        plane = int(N / D) + 1
    if N % E == 0:
        ship = int(N / E)
    else:
        ship = int(N / E) + 1
    a = max(train, bus, taxi, plane, ship)
    print(a + 4)

if __name__ == '__main__':
    main()