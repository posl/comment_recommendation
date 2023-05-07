def main():
    N = int(input())
    A = []
    for i in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    A.sort()
    ans = 0
    for i in range(N):
        if i == 0 or A[i - 1] != A[i]:
            ans += 1
    print(ans)
