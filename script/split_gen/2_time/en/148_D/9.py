def main():
    N = int(input())
    A = list(map(int, input().split()))
    # print(N, A)
    B = []
    for i in range(N):
        B.append((A[i], i))
    B.sort(key=lambda x: x[0])
    # print(B)
    ans = 0
    prev = -1
    for i in range(N):
        if B[i][1] < prev:
            ans += 1
        else:
            prev = B[i][1]
    print(ans)
