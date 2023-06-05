def solve():
    n = int(input())
    A = []
    B = []
    for i in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_time = 10**9
    for i in range(n):
        for j in range(n):
            if i == j:
                min_time = min(min_time, A[i]+B[j])
            else:
                min_time = min(min_time, max(A[i], B[j]))
    print(min_time)

if __name__ == '__main__':
    solve()