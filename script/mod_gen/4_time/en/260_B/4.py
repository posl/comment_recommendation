def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i] + B[i] for i in range(N)]
    D = sorted(range(N), key=lambda k: C[k], reverse=True)
    E = sorted(D[:X])
    F = sorted(D[X:X+Y])
    G = sorted(D[X+Y:X+Y+Z])
    H = sorted(D[X+Y+Z:])
    print('\n'.join([str(i+1) for i in E+F+G]))

if __name__ == '__main__':
    main()