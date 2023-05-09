def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    A.append(0)
    ans = 0
    for i in range(N):
        if A[i] == A[i+1]:
            continue
        else:
            ans += 1
        if ans >= K:
            break
    print(ans)
