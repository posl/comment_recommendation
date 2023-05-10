def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for i in range(Q)]
    
    total = sum(A)
    for i in range(Q):
        B = BC[i][0]
        C = BC[i][1]
        count = A.count(B)
        total += (C-B)*count
        print(total)
        A = [C if a == B else a for a in A]

if __name__ == '__main__':
    main()