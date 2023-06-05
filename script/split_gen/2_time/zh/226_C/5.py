def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()[1:])))
    A.sort()
    ans = 1
    for i in range(N - 1):
        if A[i] != A[i + 1]:
            ans += 1
    print(ans)
