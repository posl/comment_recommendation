def main():
    A,B,C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    n = 0
    while A != 100 and B != 100 and C != 100:
        n += 1
        if A == 0:
            A += 1
            B -= 1
            C -= 1
        elif B == 0:
            B += 1
            A -= 1
            C -= 1
        elif C == 0:
            C += 1
            A -= 1
            B -= 1
        else:
            i = random.randint(1,3)
            if i == 1:
                A += 1
                B -= 1
                C -= 1
            elif i == 2:
                B += 1
                A -= 1
                C -= 1
            else:
                C += 1
                A -= 1
                B -= 1
    print(n)

if __name__ == '__main__':
    main()