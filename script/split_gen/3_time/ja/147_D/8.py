def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        #iビット目が立っている数を数える
        cnt = 0
        for j in range(N):
            if A[j] >> i & 1:
                cnt += 1
        #iビット目が立っている数がcnt個あるとき、iビット目に1を立てたときのXORの回数はcnt*(N-cnt)
        #例えばiビット目に1を立てたときのXORの回数は、iビット目が0のときの数と同じになる
        #iビット目が1のときの数は、iビット目が0のときの数とXORを取ったときにiビット目が1になる
        #iビット目が1のときの数は、iビット目が1のときの数とXORを取ったときにiビット目が0になる
        #よって、iビット目が1のときの数は、iビット目が0のときの数と同じになる
        ans += cnt * (N - cnt) * pow(2, i, MOD)
        ans %= MOD
    print(ans)
solve()
