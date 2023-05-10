def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    child = [0] * N
    adult = [0] * N
    for i in range(N):
        if S[i] == '0':
            child[i] = W[i]
        else:
            adult[i] = W[i]
    child = sorted(child, reverse=True)
    adult = sorted(adult, reverse=True)
    for i in range(1, N):
        child[i] += child[i-1]
        adult[i] += adult[i-1]
    ans = 0
    for i in range(N):
        if i == 0:
            if child[i] > adult[i]:
                ans += 1
        else:
            if child[i] + adult[i-1] > adult[i] + child[i-1]:
                ans += 1
    print(ans)
