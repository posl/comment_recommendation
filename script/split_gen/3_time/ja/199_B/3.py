def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for x in range(1,1001):
        for i in range(N):
            if A[i] > x or x > B[i]:
                break
        else:
            ans += 1
    print(ans)
main()
