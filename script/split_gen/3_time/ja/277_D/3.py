def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [0] * M
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(M):
        if B[i] == 0:
            ans = i
            break
    if ans == 0:
        ans = M
    print(ans)
