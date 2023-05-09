def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(S[i]-sum(A))
    print(" ".join([str(a) for a in A]))

if __name__ == '__main__':
    main()