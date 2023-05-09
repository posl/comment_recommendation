def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #累積和を求める
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    #S[i]をMで割った余りを求める
    R = [0]*(N+1)
    for i in range(N+1):
        R[i] = S[i] % M
    #Rの値ごとに出現回数を求める
    from collections import Counter
    C = Counter(R)
    #Rの値ごとに出現回数を求める
    ans = 0
    for v,c in C.items():
        ans += c*(c-1)//2
    print(ans)
