def main():
    N = int(input())
    S = input()
    Q = int(input())
    #print(N, S, Q)
    #print()
    T = []
    A = []
    B = []
    for i in range(Q):
        t, a, b = map(int, input().split())
        T.append(t)
        A.append(a)
        B.append(b)
    #print(T, A, B)
    #print()
    #print

if __name__ == '__main__':
    main()