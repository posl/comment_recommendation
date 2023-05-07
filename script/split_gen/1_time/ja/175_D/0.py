def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    for i in range(N):
        P[i] -= 1
    ans = -10 ** 18
    for i in range(N):
        score = 0
        visited = [False] * N
        visited[i] = True
        score += C[i]
        j = P[i]
        while not visited[j]:
            visited[j] = True
            score += C[j]
            j = P[j]
        if score <= 0:
            continue
        loop = 0
        k = P[j]
        while k != j:
            loop += 1
            k = P[k]
        loop += 1
        #print(i, score, loop)
        if K < loop:
            continue
        score *= (K - loop) // loop
        k = P[j]
        while k != j:
            score += C[k]
            k = P[k]
        score += C[j]
        ans = max(ans, score)
    print(ans)
