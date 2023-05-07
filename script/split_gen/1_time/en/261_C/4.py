def main():
    N = int(input())
    S = [input() for _ in range(N)]
    cnt = {}
    for s in S:
        if s in cnt:
            cnt[s] += 1
            print(s + '(' + str(cnt[s]) + ')')
        else:
            cnt[s] = 0
            print(s)
