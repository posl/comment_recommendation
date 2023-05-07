def main():
    N, W = map(int, input().split())
    S = []
    T = []
    P = []
    for i in range(N):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)
    #print(S, T, P)
    ans = "Yes"
    # 0~200000における人数をカウントする
    people = [0] * 200001
    for i in range(N):
        people[S[i]] += P[i]
        people[T[i]] -= P[i]
    #print(people)
    # 累積和を取る
    for i in range(200000):
        people[i+1] += people[i]
    #print(people)
    # 0~200000における人数がWを超えているか判定する
    for i in range(200001):
        if people[i] > W:
            ans = "No"
            break
    print(ans)
