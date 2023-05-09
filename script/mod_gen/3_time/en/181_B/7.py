def main():
    N = int(input())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    print(sum(B)-sum(A)+N)

if __name__ == '__main__':
    main()