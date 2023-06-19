def main():
    X = int(input())
    A = 0
    B = 0
    for a in range(0, 1000):
        for b in range(0, 1000):
            if a**5-b**5 == X:
                A = a
                B = -b
            elif a**5-b**5 == -X:
                A = a
                B = b
    print(A, B)
main()
