def solve():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    total = 0
    for i in range(N):
        total += A[i]/B[i]
    total /= 2
    dist = 0
    for i in range(N):
        if total >= A[i]/B[i]:
            total -= A[i]/B[i]
            dist += A[i]
        else:
            dist += B[i]*total
            break
    print(dist)
solve()

if __name__ == '__main__':
    solve()