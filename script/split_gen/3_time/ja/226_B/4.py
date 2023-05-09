def main():
    N = int(input())
    A = []
    for i in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    A.sort()
    A.append([])
    ans = 0
    for i in range(N):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)
