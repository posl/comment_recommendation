def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (i+j) % 2 == 0:
                if (i+j) <= (A+B) and (A+B) <= (i+j+N):
                    print("#", end="")
                else:
                    print(".", end="")
            else:
                if (i-j) <= (A-B) and (A-B) <= (i-j+N):
                    print("#", end="")
                else:
                    print(".", end="")
        print()

if __name__ == '__main__':
    main()