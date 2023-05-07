def main():
    N = int(input())
    A = [0] * (N+1)
    B = [0] * (N+1)
    for i in range(N-1):
        a,b = map(int,input().split())
        A[a] += 1
        B[b] += 1
    if A.count(1) > 1:
        print(1)
        return
    if B.count(1) > 1:
        print(1)
        return
    for i in range(1,N+1):
        if A[i] == 1:
            print(i)
            return
    for i in range(1,N+1):
        if B[i] == 1:
            print(i)
            return

if __name__ == '__main__':
    main()