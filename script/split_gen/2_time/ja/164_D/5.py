def main():
    S = input()
    mod = 2019
    cnt = [0] * mod
    cnt[0] = 1
    a = 1
    s = 0
    for i in range(len(S)-1, -1, -1):
        s += int(S[i]) * a
        s %= mod
        cnt[s] += 1
        a *= 10
        a %= mod
    ans = 0
    for i in range(mod):
        ans += cnt[i] * (cnt[i] - 1) // 2
    print(ans)
