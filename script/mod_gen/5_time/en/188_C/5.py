def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted(A)
    C = B[-1]
    D = B[-2]
    E = A.index(D)
    print(E+1)
main()

if __name__ == '__main__':
    main()