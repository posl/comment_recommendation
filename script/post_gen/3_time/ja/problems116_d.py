Synthesizing 1/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    sushi = []
    for i in range(N):
        t, d = map(int, input().split())
        sushi.append((t, d))
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind = set()
    kind_sushi = []
    ans = 0
    for i in range(K):
        ans += sushi[i][1]
        if sushi[i][0] not in kind:
            kind.add(sushi[i][0])
            kind_sushi.append(sushi[i])
    ans += len(kind)**2
    kin
