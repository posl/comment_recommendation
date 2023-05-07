def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    A = []
    B = []
    for i in range(N):
        A.append(i+1)
        B.append(i+1)
    a = 0
    b = 0
    for i in range(N):
        a += (A.index(P[i])) * (math.factorial(N-i-1))
        A.remove(P[i])
        b += (B.index(Q[i])) * (math.factorial(N-i-1))
        B.remove(Q[i])
    print(abs(a-b))

if __name__ == '__main__':
    main()