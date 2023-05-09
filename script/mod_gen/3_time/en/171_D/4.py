def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    B = []
    C = []
    for i in range(Q):
        b,c = map(int,input().split())
        B.append(b)
        C.append(c)
    for i in range(Q):
        A = [C[i] if x == B[i] else x for x in A]
        print(sum(A))

if __name__ == '__main__':
    main()