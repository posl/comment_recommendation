def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 1
    for s in S:
        if s == 'OR':
            ans += 2**(S.count('OR'))
    print(ans)
