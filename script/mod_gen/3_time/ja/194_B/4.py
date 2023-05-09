def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    Amin = min(A)
    Bmin = min(B)
    for i in range(N):
        if A[i] == Amin and B[i] == Bmin:
            print(min(Amin + Bmin, max(Amin, Bmin), max(Amin, Bmin)))
            break
        elif A[i] == Amin or B[i] == Bmin:
            print(max(Amin, Bmin))
            break

if __name__ == '__main__':
    main()