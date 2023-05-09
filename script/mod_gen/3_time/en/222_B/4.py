def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(len(A)):
        if A[i] < P:
            count += 1
    print(count)

if __name__ == '__main__':
    main()