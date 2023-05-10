def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [6, 2, 3]
    # N = 3
    D = {}
    for i in range(N):
        if A[i] in D:
            D[A[i]] += 1
        else:
            D[A[i]] = 1
    # print(D)
    # D = {6: 1, 2: 1, 3: 1}
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i] % A[j] == 0 and A[i] // A[j] in D:
                ans += D[A[i] // A[j]]
    print(ans)
