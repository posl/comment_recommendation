def main():
    N, Q = map(int, input().split())
    S = input()
    #ACの数を数える
    cnt = [0 for i in range(N+1)]
    for i in range(N-1):
        if S[i] + S[i+1] == "AC":
            cnt[i+1] = cnt[i] + 1
        else:
            cnt[i+1] = cnt[i]
    #print(cnt)
    for i in range(Q):
        l, r = map(int, input().split())
        print(cnt[r-1] - cnt[l-1])
