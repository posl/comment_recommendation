def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    for i in range(P, Q+1):
        for j in range(R, S+1):
            if (A <= i <= B) and (A <= j <= B):
                print("#", end="")
            elif (A <= i+j-N-1 <= B) and (A <= j-i+N-1 <= B):
                print("#", end="")
            else:
                print(".", end="")
        print()

if __name__ == '__main__':
    main()