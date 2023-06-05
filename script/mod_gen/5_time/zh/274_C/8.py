def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0 for i in range(2*N+1)]
    for i in range(N):
        result[A[i]] = 1
    for i in range(2*N+1):
        if result[i] == 1:
            print(0)
        else:
            print(get_distance(i, result))

if __name__ == '__main__':
    main()