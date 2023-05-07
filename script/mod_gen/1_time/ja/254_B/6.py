def main():
    N = int(input())
    A = [1]
    for _ in range(N):
        print(*A)
        A = [1] + [A[i] + A[i+1] for i in range(len(A)-1)] + [1]

if __name__ == '__main__':
    main()