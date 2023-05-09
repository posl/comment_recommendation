def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a = dict()
    b = dict()
    for i in range(N):
        a[A[i]] = i
        b[B[i]] = i
    count = 0
    for i in range(N):
        if A[i] == B[i]:
            count += 1
    print(count)
    count = 0
    for i in range(N):
        if A[i] in b and i != b[A[i]]:
            count += 1
    print(count)
main()

if __name__ == '__main__':
    main()