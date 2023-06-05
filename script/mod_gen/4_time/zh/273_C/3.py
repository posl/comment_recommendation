def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    count = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            if A[j] > A[i]:
                count[i] += 1
    #print(count)
    for i in range(N):
        print(count.count(i))

if __name__ == '__main__':
    solve()