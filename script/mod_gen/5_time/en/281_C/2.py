def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += A[i]
    count = 0
    ans = 0
    for i in range(N):
        count += A[i]
        if count >= T:
            ans = i + 1
            break
    if count == T:
        print(ans, A[ans - 1])
    else:
        print(ans, A[ans - 1] - (count - T))
main()
