def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    ans = T
    for i in range(N):
        for j in range(N):
            if T[i] < T[j] and T[i] + S[i] < T[j]:
                ans[i] = T[j]
                break
        else:
            continue
        break
    for i in range(N):
        print(ans[i])
