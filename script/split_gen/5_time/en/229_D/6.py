def main():
    S = input()
    K = int(input())
    S = S.replace('..', '.')
    S = S.replace('X', ' ')
    S = S.split(' ')
    S = [len(x) for x in S]
    S = [x for x in S if x > 0]
    S = [x + 1 for x in S]
    S = [0] + S + [0]
    ans = 0
    for i in range(len(S) - K - 1):
        ans = max(ans, sum(S[i:i + K + 1]))
    print(ans)
