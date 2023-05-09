def main():
    S = input()
    N = len(S)
    if N <= 3:
        if int(S) % 2019 == 0:
            print(N * (N + 1) // 2)
        else:
            print(0)
        return
    S = list(map(int, S))
    S = [x * pow(10, i, 2019) for i, x in enumerate(S[::-1])]
    S = [sum(S[i:]) % 2019 for i in range(N)]
    ans = 0
    count = {}
    for s in S:
        if s in count:
            ans += count[s]
            count[s] += 1
        else:
            count[s] = 1
    print(ans)
