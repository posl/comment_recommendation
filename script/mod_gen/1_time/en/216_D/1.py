def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for i in range(M):
        k = int(input())
        K.append(k)
        a = list(map(int, input().split()))
        A.append(a)
    B = [0] * N
    for i in range(M):
        B[A[i][0]-1] += 1
        B[A[i][1]-1] += 1
    for b in B:
        if b % 2 == 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()