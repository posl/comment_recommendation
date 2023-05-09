def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(sum([B[C[i]-1] == A[i] for i in range(N)]))

if __name__ == '__main__':
    main()