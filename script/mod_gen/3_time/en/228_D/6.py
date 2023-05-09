def main():
    N = 2**20
    Q = int(input())
    A = [-1]*N
    for _ in range(Q):
        t,x = map(int,input().split())
        if t == 1:
            h = x
            while A[h%N] != -1:
                h += 1
            A[h%N] = x
        else:
            print(A[x%N])
    return

if __name__ == '__main__':
    main()