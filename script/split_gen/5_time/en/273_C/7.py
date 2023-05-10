def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    A.append(0)
    count = 1
    ans = [0 for i in range(N)]
    for i in range(1, N+1):
        if A[i-1] != A[i]:
            ans[count-1] = i - count
            count = i + 1
    print(*ans, sep='\n')
