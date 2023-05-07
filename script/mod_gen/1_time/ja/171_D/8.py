def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(Q):
        B, C = map(int, input().split())
        sum += (C - B) * A.count(B)
        print(sum)
        A = list(map(lambda x: C if x == B else x, A))
main()

if __name__ == '__main__':
    main()