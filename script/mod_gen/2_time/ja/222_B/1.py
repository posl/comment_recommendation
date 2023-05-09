def main():
    N, P = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if A[i] < P:
            count += 1
    print(count)
main()

if __name__ == '__main__':
    main()