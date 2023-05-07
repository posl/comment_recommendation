def main():
    S = input()
    Q = int(input())
    queries = [list(map(int, input().split())) for _ in range(Q)]
    A, B, C = S.count("A"), S.count("B"), S.count("C")
    for t, k in queries:
        if t % 3 == 0:
            if k <= A:
                print("A")
            elif k <= A + B:
                print("B")
            else:
                print("C")
        elif t % 3 == 1:
            if k <= B:
                print("B")
            elif k <= A + B:
                print("A")
            else:
                print("C")
        else:
            if k <= C:
                print("C")
            elif k <= A + C:
                print("A")
            else:
                print("B")

if __name__ == '__main__':
    main()